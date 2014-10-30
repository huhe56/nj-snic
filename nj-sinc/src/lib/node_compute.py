'''
Created on Aug 14, 2013

@author: huhe
'''

import re, time

from main.define import Define
from lib.redhat import RedHat
from lib.util import Util


class NodeCompute(RedHat):
    '''
    classdocs
    '''


    def __init__(self, hostname, username=Define.NODE_USERNAME_ROOT, password=Define.SERVER_DEFAULT_PASSWORD):
        '''
        Constructor
        '''
        RedHat.__init__(self, hostname, username, password)        
        self._current_output = None
        self._vf_used_count_equal_dict = {}
        self._ucsm_server_vnic_dict = None
        self._usnic_status_dict = {}
        self._usnic_eth_list = {}
        self._total_cpu_core_count = None
        self._np = None
        self._min_total_cpu_core_count = None
        self._vf_sharing = True

    @staticmethod
    def wait_for_node_to_boot_up(node_ip):
        node = None
        probe_max_count = 10
        try_count = 1
        interval = 60
        while try_count <= probe_max_count:
            try:
                node = NodeCompute(node_ip)
                if not node.get_ssh():
                    Util._logger.info("probe times: " + str(try_count))
                    try_count = try_count + 1
                    time.sleep(interval)
                else:
                    #node.get_ssh().send_expect_prompt("uptime")
                    return node
            except:
                Util._logger.info("exception is raised in ssh")
                try_count = try_count + 1
                time.sleep(interval)
        raise Exception("Failed to ssh to " + node_ip + " for " + probe_max_count + " times")


    def get_ifconfig_data(self):
        self._ssh.send_expect_prompt("ifconfig -a")
        output = self._ssh.get_output()
        line_list = output.split("\r\n")
        p_eth = re.compile("(?P<eth>^eth[0-9\.]+)")
        p_ip  = re.compile("(?<=inet addr:)((?:\d{1,3}\.){3}\d{1,3})")
        p_mtu = re.compile("(?<=MTU:)(\d+)")
        eth_index = None
        for line in line_list:
            m = p_eth.search(line)
            if m:
                eth_index = m.groups("eth")[0]
                self._usnic_eth_list[eth_index] = {}
            elif eth_index:
                m = p_ip.search(line)
                if m:
                    ip = m.groups("ip")[0]
                    self._usnic_eth_list[eth_index]["ip"] = ip
                m = p_mtu.search(line)
                if m:
                    mtu = m.groups("mtu")[0]
                    self._usnic_eth_list[eth_index]["mtu"] = int(mtu)
                    eth_index = None
        self._logger.debug(self._usnic_eth_list)
        
    
    def get_snic_stats(self):
        self._ssh.send_expect_prompt('mount -t debugfs nodev /sys/kernel/debug')
        self._ssh.send_expect_prompt('cd /sys/kernel/debug')
        self._ssh.send_expect_prompt('cat snic/statistics/host0/stats')
        output = self._ssh.get_output()
        
        output_line_list = output.split(Define.PATTERN_NEW_LINE)
        
        key_count = 0
        for line in output_line_list:
            if ':' in line:
                item_list = line.split(':')
                if len(item_list) == 2:
                    key = item_list[0].strip()
                    if key in Define.SNIC_STATS_ERROR_LIST:
                        self._logger.info(line)
                        key_count += 1
                        count = int(item_list[1].strip())
                        if count != 0:
                            self._logger.error(line)
        
        if key_count != len(Define.SNIC_STATS_ERROR_LIST):
            self._logger.error('some keys are not found')             
                        
    
    def setup_medusa(self):
        file_json_step = Define.PATH_SNIC_JSON_LINUX + "medusa_setup.json"
        Util.run_step_list(self._ssh, file_json_step)
            
            
    def start_medusa(self):
        if self._hostname.endswith('1'):
            file_json_step = Define.PATH_SNIC_JSON_LINUX + "medusa_start_1lun.json"
        else:
            file_json_step = Define.PATH_SNIC_JSON_LINUX + "medusa_start_2lun.json"
        Util.run_step_list(self._ssh, file_json_step)
        
        
    def stop_medusa(self):
        file_json_step = Define.PATH_SNIC_JSON_LINUX + "medusa_stop.json"
        Util.run_step_list(self._ssh, file_json_step)
        
    
        
    
        
        
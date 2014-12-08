'''
Created on Aug 26, 2014

@author: huhe
'''

import sys
from main.define import Define
from cmd.ucsm.server import sp_define
from lib.node_head import NodeHead
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    if False:
        head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
        file_json_step = Define.PATH_SNIC_JSON_LINUX + "clear_ssh_known_host.json"   
        Util.run_step_list(head_node.get_ssh(), file_json_step)
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        print "\n"
        print '-'*30 + host_ip + '-'*30
        try:
            node = NodeCompute(host_ip)
            node.exit()
            result_dict[host_ip] = True
        except:
            result_dict[host_ip] = False
            print "Unexpected error:", sys.exc_info()[0]
    
    print "\n"
    Util.print_host_status(result_dict)
    
        
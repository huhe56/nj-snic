'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, time, pexpect
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

def run_cmd(host_ip, cmd_list, cmd_sleep):
    print "\n\n"
    print '='*30 + host_ip + '='*30
    node = NodeCompute(host_ip)
    for cmd in cmd_list:
        node.run_cmd(cmd)
        time.sleep(cmd_sleep)
        node.run_cmd("")
        node.run_cmd("")
        node.run_cmd(cmd)
        node.run_cmd("")
        node.run_cmd("")
    node.exit()
    

if __name__ == '__main__':
    
    cmd1 = "tail /root/tools/medusa/shell/host*.log"
    cmd2 = "tail /root/tools/medusa/shell-sdb/host*.log"
    cmd_sleep = 10
    
    lun_type = sp_define.MEDUSA_TEST_LUN_TYPE
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        try:
            cmd_list = []
            if lun_type == 1:
                cmd_list.append(cmd1)
            elif lun_type == 2:
                cmd_list.append(cmd2)
            elif lun_type == 3:
                cmd_list.append(cmd1)
                cmd_list.append(cmd2)
            run_cmd(host_ip, cmd_list, cmd_sleep)
            result_dict[host_ip] = True
        except (KeyboardInterrupt, AttributeError, pexpect.TIMEOUT):
                print "ERROR: Timeout"
                result_dict[host_ip] = False
        except:
            print "Unexpected error:", sys.exc_info()[0]
            result_dict[host_ip] = False
            
    print "\n\n\n"
    Util.print_host_status(result_dict)
'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, time
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    cmd1 = "grep ERR /root/tools/medusa/shell/host*.log"
    cmd2 = "grep ERR /root/tools/medusa/shell-sdb/host*.log"
    
    cmd1 = "grep -i error /root/tools/medusa/shell/host*.log | grep -v label"
    cmd2 = "grep -i error /root/tools/medusa/shell-sdb/host*.log | grep -v label"
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip.startswith('20.200.10.1'): continue
        print "\n\n"
        print '='*30 + host_ip + '='*30
        try:
            node = NodeCompute(host_ip)
            node.run_cmd(cmd1)
            node.run_cmd("")
            if host_ip.endswith('2'):
                node.run_cmd("")
                print '-'*15 + host_ip + '-'*15
                node.run_cmd(cmd2)
                node.run_cmd("")
            node.exit()
            result_dict[host_ip] = True
        except:
            print "Unexpected error:", sys.exc_info()[0]
            result_dict[host_ip] = False
            
    print "\n\n\n"
    Util.print_host_status(result_dict)
'''
Created on Aug 26, 2014

@author: huhe
'''

import sys
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip.startswith('20.200.10.112'): continue
        print "\n"
        print '-'*30 + host_ip + '-'*30
        try:
            node = NodeCompute(host_ip)
            node.start_medusa()
            node.exit()
            result_dict[host_ip] = True
        except:
            result_dict[host_ip] = False
            print "Unexpected error:", sys.exc_info()[0]
            
    print "\n"
    Util.print_host_status(result_dict)
            
    
    
        
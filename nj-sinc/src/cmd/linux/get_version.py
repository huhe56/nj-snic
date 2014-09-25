'''
Created on Aug 26, 2014

@author: huhe
'''

from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip.startswith('20.200.10.1'): continue
        print "\n"
        print '-'*30 + host_ip + '-'*30
        try:
            node = NodeCompute(host_ip)
            os_version = node.get_os_version()
            snic_version = node.get_snic_version()
            print '='*20 + snic_version + ", " + os_version
            node.exit()
            result_dict[host_ip] = True
        except:
            result_dict[host_ip] = False
            
    print "\n"
    Util.print_host_status(result_dict)
            
    
    
        
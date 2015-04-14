'''
Created on Aug 26, 2014

@author: huhe
'''

from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute


if __name__ == '__main__':
    
    host_ip_list = sp_define.get_all_host_ip()
    print host_ip_list
    for host_ip in host_ip_list:
        node = NodeCompute(host_ip)
        node.get_snic_stats()
        node.exit()
    
    
        
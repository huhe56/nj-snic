'''
Created on Aug 26, 2014

@author: huhe
'''

from main import define
from main.define import Define
from cmd.ucsm.server import sp_define
from lib.util import Util
from lib.node_head import NodeHead


if __name__ == '__main__':
    
    define.PEXPECT_OUTPUT_STDOUT = False
        
    head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
    
    host_ip_list = sp_define.get_all_host_ip()
    print host_ip_list
    for host_ip in host_ip_list:
        if not host_ip.startswith('20.200.10.1'): continue
        status = Util.ping(head_node.get_ssh(), host_ip, 2)
        if status:
            print "Passed: " + host_ip + " is up"
        else:
            print "Failed: " + host_ip + " is down"
    
    
        
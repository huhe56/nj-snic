'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from cmd.ucsm.server import sp_define
from lib.util import Util
from lib.node_head import NodeHead


if __name__ == '__main__':
    
    param = {}    
    head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
    
    host_ip_list = sp_define.get_all_host_ip()
    print host_ip_list
    for host_ip in host_ip_list:
        param['tag_host_ip'] = host_ip
        if host_ip.startswith('20.200.10.1'):
            try:
                file_json_step = Define.PATH_SNIC_JSON_LINUX + "get_uptime.json"   
                Util.run_step_list(head_node.get_ssh(), file_json_step, param)
            except:
                pass

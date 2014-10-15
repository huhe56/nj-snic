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
    
    skipped_host_list = ['20.200.10.111', '20.200.10.131', '20.200.10.132']
    
    head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
    file_json_step = Define.PATH_SNIC_JSON_LINUX + "var_log_msg_clear.json"   
    Util.run_step_list(head_node.get_ssh(), file_json_step)
    
    host_ip_list = sp_define.get_all_host_ip()
    print host_ip_list
    for host_ip in host_ip_list:
        param['tag_host_ip'] = host_ip
        if host_ip.startswith('20.200.10.14') or host_ip in skipped_host_list: continue
        try:
            file_json_step = Define.PATH_SNIC_JSON_LINUX + "var_log_msg_get.json"   
            Util.run_step_list(head_node.get_ssh(), file_json_step, param)
        except:
            pass
    
    
        
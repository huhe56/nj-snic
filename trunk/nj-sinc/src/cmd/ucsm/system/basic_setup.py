'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    
    
    
    '''
    eth0: pxe    vlan10
    eth1: medusa vlan2000
    '''
    data_vlan_start = Define.TEST_BED * 100 + 20 + 3
    data_vlan_end   = data_vlan_start + 5
    eth_vlan_list = range(data_vlan_start, data_vlan_end)
    eth_vlan_list.insert(0, 113)
    eth_vlan_list.insert(0, 2000)
    eth_vlan_list.insert(0, 10)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "vlan.txt"  
    
    for vlan_id in eth_vlan_list: 
        param = {"tag_vlan_name": "vlan"+str(vlan_id), "tag_vlan_id": str(vlan_id)}
        Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
        
    '''
    enable server and uplink ports, vlan10
    '''
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "basic_setup.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step)
    
    ucsm.exit()
    

    
    
        
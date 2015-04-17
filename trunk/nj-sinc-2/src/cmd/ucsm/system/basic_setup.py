'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from cmd.ucsm.server import sp_define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    
    '''
    eth0: pxe    vlan10
    eth1: medusa vlan2000
    eth2: pxe    vlan114
    '''
    
    eth_vlan_list = Define.VLAN_MGMT + Define.VLAN_VM
    eth_vlan_set = set(eth_vlan_list)
    eth_vlan_list = list(eth_vlan_set)

    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "vlan.txt"  
    
    for vlan_id in eth_vlan_list: 
        param = {"tag_vlan_name": "vlan"+str(vlan_id), "tag_vlan_id": str(vlan_id)}
        Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
        
    '''
    enable server and uplink ports
    '''
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "basic_setup.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step)
    
    ucsm.exit()
    

    
    
        
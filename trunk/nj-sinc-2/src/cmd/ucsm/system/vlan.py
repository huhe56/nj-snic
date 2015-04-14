'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    '''
    eth0: pxe    vlan10
    eth1: medusa vlan2000
    '''
    vlan_id_list = range(122, 128)
    vlan_id_list.append(113)
    vlan_id_list.append(2000)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "vlan.txt"  
    
    for vlan_id in vlan_id_list: 
        param = {"tag_vlan_name": "vlan"+str(vlan_id), "tag_vlan_id": str(vlan_id)}
        Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
        
    ucsm.exit()
    

    
    
        
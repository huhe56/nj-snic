'''
Created on Aug 26, 2014

@author: huhe
'''

import pprint
from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define



if __name__ == '__main__':
    
    param = sp_define.param
    
    chassis_id      = str(param['chassis_id']).zfill(2)
    cartridge_id    = str(param['cartridge_id']).zfill(2)
    server_id       = str(param['server_id']).zfill(2)
    
    server_full_id_list = [chassis_id, cartridge_id, server_id]
    server_full_id  = ''.join(server_full_id_list)
    param['tag_service_profile_name'] = '-'.join(['sp', chassis_id, cartridge_id, server_id])
    
    eth_id_number_list = range(2, 8)
    eth_id_number_list.append(1790)
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    for eth_id_number in eth_id_number_list: 
        print ("--------" + str(eth_id_number))
        eth_id = str(eth_id_number).zfill(2)
        if eth_id_number  == 1790:
            eth_id = '01'
        eth_full_id_list = [chassis_id, cartridge_id, server_id, eth_id]
        eth_full_id = ''.join(eth_full_id_list)
        vlan_id = str(210 + eth_id_number)
        param['tag_mac_address'] = ':'.join([param['mac_prefix'], ':'.join(eth_full_id_list)])
        param["tag_eth_name"] = ''.join([param["eth_pxe_name_prefix"], vlan_id])
        param["tag_eth_vlan"] = ''.join(["vlan", vlan_id])
    
        if eth_id_number == 1790 or eth_id_number % 2 == 1:
            param["tag_eth_fabric"] = 'b'
        else:
            param["tag_eth_fabric"] = 'a'
        pprint.pprint(param)
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_eth_vlan.txt"   
        Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    

    
    
        
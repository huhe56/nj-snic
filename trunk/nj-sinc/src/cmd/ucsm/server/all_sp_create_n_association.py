'''
Created on Aug 26, 2014

@author: huhe
'''

import time
import pprint

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param  = sp_define.param
    
    #pprint.pprint(sp_define.config)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ucsm_ssh = ucsm.get_ssh()
    
    initiator_ip_suffix  = 40
    initiator_iqn_suffix = 100
    
    for chassis_id, chassis in sp_define.config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():
                if chassis_id != 1: continue
                param['chassis_id']     = chassis_id
                param['cartridge_id']   = cartridge_id
                param['server_id']      = server_id
                
                param['tag_boot_policy'] = server['boot_policy']
                
                #pprint.pprint(param)
                sp_define.create_service_profile(ucsm_ssh, param)
                
                eth_cnt = server['eth_cnt']
                if eth_cnt > 0:
                    sp_define.create_eth_if_in_service_profile(ucsm_ssh, param, eth_cnt) 
                    
                if 'lun' in server.keys():
                    lun = server['lun']
                    sp_define.create_lun_in_service_profile(ucsm_ssh, param, lun)
                elif 'storage_profile' in server.keys():
                    storage_profile = server['storage_profile']
                    sp_define.create_storage_profile_in_service_profile(ucsm_ssh, param, storage_profile)
                
                initiator_ip_suffix  += 1
                initiator_iqn_suffix += 1
                if server['boot_policy'].startswith('iscsi'):
                    param['tag_initiator_ip_suffix']  = str(initiator_ip_suffix)
                    param['tag_initiator_iqn_suffix'] = str(initiator_iqn_suffix)
                    sp_define.create_iscsi_in_service_profile(ucsm_ssh, param)
                
                #sp_define.associate_service_profile(ucsm_ssh, param)
                #time.sleep(300)
                
    ucsm.exit()
    

    
    
        
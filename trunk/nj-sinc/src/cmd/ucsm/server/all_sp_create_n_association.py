'''
Created on Aug 26, 2014

@author: huhe
'''

import time

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param  = sp_define.param
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ucsm_ssh = ucsm.get_ssh()
    
    for chassis_id, chassis in sp_define.config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():
                disk_size   = str(server['disk_size'])
                raid_level  = server['raid_level']
                all_eth     = False
                if 'all_eth' in server.keys():
                    all_eth = server['all_eth']
                    
                disk_policy = sp_define.raid_level_disk_group_config_policy_dict[raid_level]['policy_name']
    
                param['chassis_id']     = chassis_id
                param['cartridge_id']   = cartridge_id
                param['server_id']      = server_id
                param['tag_eth_vlan']   = 'vlan10'
                
                param['tag_disk_size']  = disk_size
                param['tag_disk_group_config_policy_name'] = disk_policy
                
                sp_define.create_service_profile(ucsm_ssh, param)
                
                if all_eth:
                    sp_define.create_eth_if_in_service_profile(ucsm_ssh, param) 
                    
                sp_define.associate_service_profile(ucsm_ssh, param)
                time.sleep(30)
                
    ucsm.exit()
    

    
    
        
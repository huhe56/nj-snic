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
    
    for chassis_id, chassis in sp_define.config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():
                
                lun = server['lun']
                boot_policy = server['boot_policy']
                boot_policy = 'disk-pxe-' + boot_policy
                    
                eth_cnt     = 1
                if 'eth_cnt' in server.keys():
                    eth_cnt = server['eth_cnt']
                    
                param['chassis_id']     = chassis_id
                param['cartridge_id']   = cartridge_id
                param['server_id']      = server_id
                param['tag_eth_fabric']   = 'a'
                param['tag_eth_vlan']   = 'vlan10'
                param['tag_eth_order']   = '1'
                param['tag_boot_policy'] = boot_policy
                
                #pprint.pprint(param)
                sp_define.create_service_profile(ucsm_ssh, param)
                
                eth_cnt -= 1
                if eth_cnt > 0:
                    sp_define.create_eth_if_in_service_profile(ucsm_ssh, param, eth_cnt) 
                    
                sp_define.create_lun_in_service_profile(ucsm_ssh, param, lun)
                
                #sp_define.associate_service_profile(ucsm_ssh, param)
                #time.sleep(300)
                
    ucsm.exit()
    

    
    
        
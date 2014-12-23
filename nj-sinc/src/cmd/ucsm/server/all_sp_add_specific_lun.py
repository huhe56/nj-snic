'''
Created on Aug 26, 2014

@author: huhe
'''

import time
import pprint

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


LUN = {
       2: {'disk_size': 10, 'raid_level': 1},
       }

if __name__ == '__main__':
    
    param  = sp_define.param
    
    #pprint.pprint(sp_define.config)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ucsm_ssh = ucsm.get_ssh()
    
    for chassis_id, chassis in sp_define.config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():
                host_suffix = chassis_id * 100 + cartridge_id * 10 + server_id
                if not host_suffix in sp_define.HOST_SUFFIXE_LIST: continue
                param['chassis_id']     = chassis_id
                param['cartridge_id']   = cartridge_id
                param['server_id']      = server_id
                    
                sp_define.create_lun_in_service_profile(ucsm_ssh, param, LUN)
                
    ucsm.exit()
    

    
    
        
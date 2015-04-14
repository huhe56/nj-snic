'''
Created on Aug 26, 2014

@author: huhe
'''


from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param  = sp_define.param
    storage_profile = 'sp-1-lun'

    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ucsm_ssh = ucsm.get_ssh()
    
    for chassis_id, chassis in sp_define.config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            if cartridge_id < 4: continue
            for server_id, server in cartridge.iteritems():    
                param['chassis_id']     = chassis_id
                param['cartridge_id']   = cartridge_id
                param['server_id']      = server_id
                sp_define.create_storage_profile_in_service_profile(ucsm_ssh, param, storage_profile)
                                
    ucsm.exit()
    

    
    
        
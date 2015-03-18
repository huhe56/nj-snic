'''
Created on Aug 26, 2014

@author: huhe
'''


from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


MTU9K = 9000
MTU1K = 1500
MTU = MTU1K
MTU_DICT = {
       'eth10':     MTU,
       'eth2000':   MTU,
       'eth114':    MTU,
       'eth323':    MTU,
       'eth324':    MTU,
       'eth325':    MTU,
       'eth326':    MTU,
       'eth327':    MTU
       }

if __name__ == '__main__':
    
    param  = sp_define.param
        
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
                    
                sp_define.set_vnic_mtu_in_service_profile(ucsm_ssh, param, MTU_DICT)
                
    ucsm.exit()
    

    
    
        
'''
Created on Aug 26, 2014

@author: huhe
'''


from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define



ETH_IF_VLAN_NUMBER_LIST = [x for x in range(323, 328)]
ETH_IF_VLAN_NUMBER_LIST = []
ETH_IF_VLAN_NUMBER_LIST.append(2000)
ETH_IF_VLAN_NUMBER_LIST.append(114)

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
                    
                sp_define.set_vnic_no_vlan_in_service_profile(ucsm_ssh, param, ETH_IF_VLAN_NUMBER_LIST)
                
    ucsm.exit()
    

    
    
        
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
    
    chassis     = str(param['chassis_id'])
    cartridge   = str(param['cartridge_id'])
    server      = str(param['server_id'])
    
    chassis_id      = str(chassis).zfill(2)
    cartridge_id    = str(cartridge).zfill(2)
    server_id       = str(server).zfill(2)
    eth_id          = str(param['eth_pxe_name_index']).zfill(2)
    
    server_full_id_list = [chassis_id, cartridge_id, server_id]
    server_full_id  = ''.join(server_full_id_list)
    
    eth_full_id_list = [chassis_id, cartridge_id, server_id, eth_id]
    eth_full_id = ''.join(eth_full_id_list)
    
    param['tag_service_profile_name'] = '-'.join(['sp', chassis, cartridge, server])
    param['tag_local_lun'] = ''.join(['lun', server_full_id])
    param['tag_volumn_name'] = ''.join(['volumn', server_full_id])
    param['tag_mac_address'] = ':'.join([param['mac_prefix'], ':'.join(eth_full_id_list)])
    param["tag_eth_name"] = ''.join([param["eth_pxe_name_prefix"], str(param["eth_pxe_name_index"])])
    param['tag_uuid'] = ''.join([param['uuid_prefix'], server_full_id])
    
    pprint.pprint(param)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    

    
    
        
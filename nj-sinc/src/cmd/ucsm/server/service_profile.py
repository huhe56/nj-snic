'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param = sp_define.param
    
    mac_prefix  = '00:25:B5'
    uuid_prefix = '00000000-0000-0000-0000-000000'
    
    chassis_id      = str(param['chassis_id']).zfill(2)
    cartridge_id    = str(param['cartridge_id']).zfill(2)
    server_id       = str(param['server_id']).zfill(2)
    server_full_id_list = [chassis_id, cartridge_id, server_id]
    server_full_id  = ''.join(server_full_id_list)
    
    param['tag_service_profile_name'] = '-'.join(['sp', chassis_id, cartridge_id, server_id])
    param['tag_local_lun'] = ''.join(['lun', server_full_id])
    param['tag_volumn_name'] = ''.join(['volumn', server_full_id])
    param['tag_mac_address'] = ':'.join([mac_prefix, ':'.join(server_full_id_list)])
    param['tag_uuid'] = ''.join([uuid_prefix, server_full_id])
    
    print param
    
    '''
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    '''

    
    
        
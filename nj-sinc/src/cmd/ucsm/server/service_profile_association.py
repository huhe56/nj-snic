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
    
    server_full_list = [chassis, cartridge, server]
    param['tag_service_profile_name'] = '-'.join(['sp', chassis, cartridge, server])
    param['tag_server_full_id'] = '/'.join(server_full_list)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_association.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    

    
    
        
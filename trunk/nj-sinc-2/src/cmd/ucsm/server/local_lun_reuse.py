'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param = {}
    param['chassis_id']     = 1
    param['cartridge_id']   = 4
    param['server_id']      = 1
    
    param['tag_local_lun_name']     = 'lun141_1'
    param['tag_disk_policy_name']   = 'raid0striped'
    param['tag_expand_to_avail'] = 'no'
    param['tag_order']  = '1'
    param['tag_size']   = '40'
    
    param['tag_deployed_lun_name']  = 'lun141_1-1'
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    sp_define.reuse_local_lun(ucsm.get_ssh(), param)
    ucsm.exit()
    

    
    
        
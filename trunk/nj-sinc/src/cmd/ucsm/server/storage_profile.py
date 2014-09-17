'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param = sp_define.param
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    
    param['tag_storage_profile_name']     = 'sp-1-lun'
    
    param['tag_local_lun_name_1']   = 'sp1lun_1'
    param['tag_disk_policy_name_1'] = 'raid0striped'
    param['tag_expand_to_avail_1']  = 'no'
    param['tag_order_1']  = '1'
    param['tag_size_1']   = '40'
    
    param['cmd_text_file_name'] = 'storage_profile_1_lun.txt'
    
    sp_define.run(ucsm.get_ssh(), param)
    
    param['tag_storage_profile_name']     = 'sp-2-lun'
    
    param['tag_local_lun_name_1']   = 'sp2lun_1'
    param['tag_disk_policy_name_1'] = 'raid0striped'
    param['tag_expand_to_avail_1']  = 'no'
    param['tag_order_1']  = '1'
    param['tag_size_1']   = '40'
    
    param['tag_local_lun_name_2']   = 'sp2lun_2'
    param['tag_disk_policy_name_2'] = 'raid0striped'
    param['tag_expand_to_avail_2']  = 'no'
    param['tag_order_2']  = '2'
    param['tag_size_2']   = '20'
    
    param['cmd_text_file_name'] = 'storage_profile_2_lun.txt'
    
    sp_define.run(ucsm.get_ssh(), param)
    
    ucsm.exit()
    

    
    
        
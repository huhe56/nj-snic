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
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    
    param['tag_boot_policy'] = 'bp-disk-pxe-legacy'
    param['tag_boot_mode']   = 'legacy'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_disk_pxe.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    
    param['tag_boot_policy'] = 'bp-disk-pxe-uefi'
    param['tag_boot_mode']   = 'uefi'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_disk_pxe.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    
    ucsm.exit()
    

    
    
        
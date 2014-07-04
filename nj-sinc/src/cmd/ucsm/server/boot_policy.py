'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    param = {
             "tag_boot_policy": "bp-disk-pxe"
             }
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    

    
    
        
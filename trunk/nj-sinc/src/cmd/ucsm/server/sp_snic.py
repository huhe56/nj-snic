'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "sp_snic.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, 1)
    ucsm.exit()
    

    
    
        
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
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "kvm_console_ip_pool.txt"   
    Util.run_text_step(ucsm.get_ssh(), file_text_step, param)
    ucsm.exit()
    

    
    
        
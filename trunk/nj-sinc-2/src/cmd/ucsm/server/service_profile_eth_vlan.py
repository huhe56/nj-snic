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
    sp_define.create_eth_if_in_service_profile(ucsm.get_ssh(), param)
    ucsm.exit()
    

    
    
        
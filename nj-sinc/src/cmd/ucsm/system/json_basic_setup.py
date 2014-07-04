'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    file_json_step = Define.PATH_SNIC_JSON_UCSM + "basic_setup.json"   
    Util.run_step_list(ucsm.get_ssh(), file_json_step)
    ucsm.exit()
    

    
    
        
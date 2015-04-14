'''
Created on Aug 26, 2013

@author: huhe
'''

import time

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm_b = UCSM(Define.UCSM_HOSTNAME_B);
    file_json_step = Define.PATH_SNIC_JSON_UCSM + "erase_samdb.json"   
    Util.run_step_list(ucsm_b.get_ssh(), file_json_step)
    time.sleep(300)
    ucsm_b.exit()
    
    ssh = Util.wait_for_node_to_boot_up(Define.UCSM_HOSTNAME_B, Define.UCSM_DEFAULT_USERNAME, Define.UCSM_DEFAULT_PASSWORD, "show version")
    ssh.exit()

    
    
        
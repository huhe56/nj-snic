'''
Created on Aug 26, 2013

@author: huhe
'''

import time

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    ucsm_a = UCSM(Define.UCSM_HOSTNAME_A);
    file_json_step = Define.PATH_SNIC_JSON_UCSM + "reboot_fi.json"   
    Util.run_step_list(ucsm_a.get_ssh(), file_json_step)
    ucsm_a.exit()
    
    time.sleep(30)
    
    ucsm_b = UCSM(Define.UCSM_HOSTNAME_B);
    file_json_step = Define.PATH_SNIC_JSON_UCSM + "reboot_fi.json"   
    Util.run_step_list(ucsm_b.get_ssh(), file_json_step)
    ucsm_b.exit()
    
    time.sleep(180)
    
    ssh = Util.wait_for_node_to_boot_up(Define.UCSM_HOSTNAME_B, Define.UCSM_DEFAULT_USERNAME, Define.UCSM_DEFAULT_PASSWORD, "show version")
    ssh.exit()

    
    
        
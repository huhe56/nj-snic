'''
Created on Aug 26, 2014

@author: huhe
'''

import time
from main.define import Define
from lib.cruz import Cruz
from lib.cmc import CMC


if __name__ == '__main__':
    
    ssh_new = False
    
    cmc = CMC()
    file_json_step = Define.PATH_SNIC_JSON_NJ + "cmc_touch_tech_tgz.json"
    cmc.run_cmd_step(file_json_step)
    if ssh_new:
        file_json_step = Define.PATH_SNIC_JSON_NJ + "cmc_scp_ssh_new.json"
        cmc.run_cmd_step(file_json_step)
    cmc.exit()
    
    cruz = Cruz()
    file_json_step = Define.PATH_SNIC_JSON_NJ + "cruz_collect_tech.json"
    cruz.run_cmd_step(file_json_step)
    time.sleep(5)
    cruz.exit()
    
    cmc = CMC()
    file_json_step = Define.PATH_SNIC_JSON_NJ + "cmc_scp_tech_tgz.json"
    cmc.run_cmd_step(file_json_step)
    time.sleep(5)
    cmc.exit()
    
    
    
    
    
        
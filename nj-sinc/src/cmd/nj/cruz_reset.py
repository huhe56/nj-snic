'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.cruz import Cruz


if __name__ == '__main__':
    
    cruz = Cruz()
    file_json_step = Define.PATH_SNIC_JSON_NJ + "cruz_reset.json"
    cruz.run_cmd_step(file_json_step)
    cruz.exit()
    
    
        
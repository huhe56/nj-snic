'''
Created on Aug 27, 2013

@author: huhe
'''

from main.define import Define
from lib.rar import RAR

if __name__ == '__main__':
    
    rar = RAR(Define.RAR_HOSTNAME, Define.RAR_USERNAME, Define.RAR_PASSWORD)
    rar.power_cycle(Define.RAR_CHASSIS_OUTLET_ID)
    rar.exit()

    
    
    
    
    
    

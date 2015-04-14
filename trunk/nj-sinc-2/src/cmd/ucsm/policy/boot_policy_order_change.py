'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    order_lan = 2
    
    order_storage_local_any = 0
    if order_lan == 1:
        order_storage_local_any = 2
    elif order_lan == 2:
        order_storage_local_any = 1
    
    param = sp_define.param
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    sp_define.change_boot_policy_order(ucsm.get_ssh(), param, order_storage_local_any, order_lan)
    ucsm.exit()
    

    
    
        
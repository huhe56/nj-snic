'''
Created on Aug 27, 2013

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ssh = ucsm.get_ssh()
    
    Util.collect_ucsm_tech_support(ssh)
    Util.collect_chassis_tech_support(ssh)
    
    ssh.exit()
    
    
    
    

'''
Created on Aug 27, 2013

@author: huhe
'''

from main.define import Define
from lib.util import Util
from lib.ucsm import UCSM
from lib.cmc import CMC

if __name__ == '__main__':
    
    #cmc = CMC()
    #cmc.get_lsi_tty()
    #cmc.exit()
    
    ssh_new = False
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ssh = ucsm.get_ssh()
    
    if ssh_new:
        Util.collect_ssh_new(ssh)
    
    Util.collect_ucsm_tech_support(ssh)
    Util.collect_chassis_tech_support(ssh)
    
    ssh.exit()
    
    
    
    

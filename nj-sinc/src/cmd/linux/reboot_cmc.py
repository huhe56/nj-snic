'''
Created on Aug 27, 2013

@author: huhe
'''

import time
from lib.cmc import CMC

if __name__ == '__main__':
    
    i = 0
    while True:
        i += 1
        print "*"*40 + str(i) + "*"*40
        cmc = CMC()
        cmc.reboot()
        cmc.exit()
        time.sleep(600)
    
    
    
    
    
    

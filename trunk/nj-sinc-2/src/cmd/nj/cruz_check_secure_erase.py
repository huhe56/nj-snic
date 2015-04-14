'''
Created on Aug 26, 2014

@author: huhe
'''

from lib.cruz import Cruz

PHYSICAL_DRIVE_ID_LIST = [5, 6, 7, 8]


if __name__ == '__main__':
    
    cruz = Cruz()
    
    cruz.wait_for_erase_complete(PHYSICAL_DRIVE_ID_LIST)
        
    cruz.exit()
    
    
    
        
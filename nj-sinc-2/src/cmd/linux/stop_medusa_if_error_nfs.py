'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, time, subprocess
from main.define import Define
from lib.node_head import NodeHead
from lib.util import Util

ERROR_PATTERN = 'Data corruption detected'
#ERROR_PATTERN = 'kasdjflasjdlasjfd'

if __name__ == '__main__':
    
    head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_USERNAME_ROOT, Define.NODE_DEFAULT_PASSWORD)

    cmd = 'grep -i "' + ERROR_PATTERN + '" /home/export/1*/medusa/*.log'
    print cmd
    
    while True:
        head_node.run_cmd(cmd)
        shell_status = Util.check_shell_status(head_node.get_ssh())
        if shell_status:
            print '-'*30 + '>>> found pattern: ' + ERROR_PATTERN
            subprocess.call(['python', 'medusa_stop.py'])
            subprocess.call(['python', 'get_uptime.py'])
            #subprocess.call(['python', '../nj/cruz_collect_tech.py'])
            #subprocess.call(['python', '../ucsm/system/collect_tech_support.py'])
            head_node.exit()
            sys.exit()
        else:
            print "found no pattern"
        time.sleep(60)
        
        
    
    
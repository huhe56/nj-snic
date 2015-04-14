'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect, subprocess
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

ERROR_PATTERN = 'Data corruption detected'
#ERROR_PATTERN = 'error'

if __name__ == '__main__':
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        print "\n"
        print '='*30 + host_ip + '='*30
        host_ip_suffix = Util.get_ip_field(host_ip, 3)
        #cmd = 'grep -i error /mnt/' + host_ip_suffix + '/*.log | ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA
        #cmd = 'grep -i "' + ERROR_PATTERN + '" /mnt/' + host_ip_suffix + '/medusa/*.log'
        cmd = 'grep -i error /root/tools/medusa/shell-sdb/*.log ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA
        #print cmd
        try:
            node = NodeCompute(host_ip)
            node.run_cmd(cmd)
            ssh = node.get_ssh()
            shell_status = Util.check_shell_status(ssh)
            if shell_status:
                print '-'*80 + '>>> found pattern: ' + ERROR_PATTERN
                #subprocess.call(['python', 'medusa_stop.py'])
                #subprocess.call(['python', 'get_uptime.py'])
                #subprocess.call(['sh', 'get_var_log_msg_all.sh'])
                #subprocess.call(['sh', 'get_medusa_log_all.sh'])
                #subprocess.call(['python', '../nj/cruz_collect_tech.py'])
                #subprocess.call(['python', '../ucsm/system/collect_tech_support.py'])
                #sys.exit()
            else:
                print "found no pattern"
            node.exit()
            result_dict[host_ip] = True
        except (KeyboardInterrupt, AttributeError, pexpect.TIMEOUT):
            print "ERROR: Timeout"
            result_dict[host_ip] = False
        except SystemExit:
            sys.exit()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            result_dict[host_ip] = False
            
    print "\n\n\n"
    Util.print_host_status(result_dict)
    
    
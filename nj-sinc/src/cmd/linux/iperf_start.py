'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect, subprocess
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

cmd1 = 'cd /root/tools/iperf; /mnt/cmd/shell/iperf_server.sh'
cmd2 = 'cd /root/tools/iperf; /mnt/cmd/shell/iperf_client.sh'

cmd = cmd1

if __name__ == '__main__':
    
    input_param = sys.argv[1]
    if input_param == 'server':
        cmd = cmd1
    elif input_param == 'client':
        cmd = cmd2
    else:
        exit(-1)
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        print "\n"
        print '='*30 + host_ip + '='*30
        host_ip_suffix = Util.get_ip_field(host_ip, 3)
        
        #print cmd
        try:
            node = NodeCompute(host_ip)
            node.run_cmd(cmd)
            ssh = node.get_ssh()
            shell_status = Util.check_shell_status(ssh)
            if shell_status:
                print "PASSED"
            else:
                print "FAILED"
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
    
    
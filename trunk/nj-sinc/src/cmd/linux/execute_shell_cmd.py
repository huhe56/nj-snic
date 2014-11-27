'''
Created on Aug 26, 2014

@author: huhe
'''

import sys
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    cmd = None
    cmd_list = [
                'scp',
                'ntpdate 20.200.10.250',
                'find . -name *.bad -print',
                'dmesg | grep -i error | grep -v ERST',
                'grep -i error /var/log/messages* | grep -v real_update_permanent_hw_address | grep -v ERST',
                'grep -i error /root/tools/medusa/*/1*/*.log | grep -v label | grep -v "v Retry count on error" | grep -v "O loop error event handlers:" | grep -v "exit code 0"',
                ]
    cnt = 1
    if len(sys.argv) != 2 or (len(sys.argv) == 2 and sys.argv[1]) == '0':
        print "\nUsage: " + sys.argv[0] + " number\n"
        for cmd in cmd_list:
            print "\t" + str(cnt) + ": " + cmd + "\n"
            cnt += 1
    else:
        i = int(sys.argv[1]) - 1
        cmd = cmd_list[i]
    
        print "\n" + cmd
        host_ip_list = sp_define.get_all_host_ip()
        result_dict = {}
        for host_ip in host_ip_list:
            if not host_ip.startswith('20.200.10.1'): continue
            print "\n"
            print '='*30 + host_ip + '='*30
            try:
                node = NodeCompute(host_ip)
                node.run_cmd(cmd)
                node.exit()
                result_dict[host_ip] = True
            except:
                print "Unexpected error:", sys.exc_info()[0]
                result_dict[host_ip] = False
                
        print "\n\n\n"
        Util.print_host_status(result_dict)
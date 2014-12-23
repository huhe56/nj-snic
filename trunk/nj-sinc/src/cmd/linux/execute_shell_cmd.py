'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    cmd = None
    cmd_list = [
                'fdisk -l',
                'fdisk -l | grep sdb',
                'scp',
                'uptime',
                'date; ntpdate 20.200.10.250',
                'find . -name *.bad -print',
                "ps -ef | grep maim | grep -v grep",
                'dmesg | grep -i error | grep -v ERST',
                "egrep -i '" + sp_define.PATTERN_ERROR_ONLY + "' /var/log/messages* /var/log/syslog* | grep -v real_update_permanent_hw_address | grep -v ERST",
                "egrep -i '" + sp_define.PATTERN_EGREP + "' /root/tools/medusa/*/*.log " + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                "egrep -i '" + sp_define.PATTERN_EGREP + "' /root/tools/medusa/*/1*/*.log " + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                "egrep -i 'Data corruption detected' /root/tools/medusa/*/1*/*.log",
                "sed -i 's/loop=1/loop=3/' /root/tools/medusa/shell-sdb/define.sh",
                "rm -fr /root/tools/iperf/*.log",
                "rm -fr /root/tools/medusa/shell*/host* /root/tools/medusa/shell*/1*",
                "reboot",
                "sed -i 's/-t8/-t3/' /root/tools/medusa/shell-sdb/medusa-all.sh",
                "tar xvf tools.tar",
                #'grep -i error /mnt/$$host_suffix$$/tmp/messages* | grep -v real_update_permanent_hw_address | grep -v ERST',
                #'grep -i error /mnt/*/1*/*.log | ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                #'grep -i error /mnt/*/*.log | ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                #'find /mnt -name *.bad -print',
                "cd /root/tools/iperf; /mnt/cmd/shell/iperf_server.sh",
                "cd /root/tools/iperf; /mnt/cmd/shell/iperf_client.sh",
                "ps -ef | grep iperf | grep -v grep",
                "cd /root/tools/iperf; tail *.log; sleep 5; tail *.log",
                ]
    cnt = 1
    if len(sys.argv) != 2 or (len(sys.argv) == 2 and sys.argv[1]) == '0':
        print "\nUsage: " + sys.argv[0] + " number\n"
        for cmd in cmd_list:
            print "\t" + str(cnt) + ": " + cmd + "\n"
            cnt += 1
    else:
        i = int(sys.argv[1]) - 1
        host_ip_list = sp_define.get_all_host_ip()
        result_dict = {}
        for host_ip in host_ip_list:
            if not host_ip in sp_define.HOST_LIST: continue
            ip_suffix = Util.get_ip_field(host_ip, 3)
            cmd = cmd_list[i]
            #print cmd
            cmd = cmd.replace('$$host_suffix$$', ip_suffix)
            print "\n"
            print '='*30 + host_ip + '='*30
            try:
                node = NodeCompute(host_ip)
                node.run_cmd(cmd)
                node.exit()
                result_dict[host_ip] = True
            except (KeyboardInterrupt, AttributeError, pexpect.TIMEOUT):
                print "ERROR: Timeout"
                result_dict[host_ip] = False
            except:
                print "Unexpected error:", sys.exc_info()[0]
                result_dict[host_ip] = False
                
        print "\n\n\n"
        Util.print_host_status(result_dict)
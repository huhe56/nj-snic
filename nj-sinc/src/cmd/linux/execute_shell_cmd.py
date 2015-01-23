'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    medusa_log_directory_boot_lun = "/root/tools/medusa/shell/"
    medusa_log_directory_data_lun = "/data/"
    
    medusa_log_directory = medusa_log_directory_boot_lun
    
    cmd = None
    cmd_list = [
                "reboot",
                'dmesg | grep -i error | grep -v ERST | grep -v errors=remount-ro',
                'lsblk',
                'date; ntpdate 20.200.10.250',
                'service network restart',
                'mount /dev/vg_data/volume_data /data',
                "ps -ef | grep maim | grep -v grep",
                "ps -ef | grep iperf | grep -v grep",
                
                '/bin/rm -fr /root/tools/iperf/*.log /root/tools/medusa/shell/* /data/*',
                '/bin/rm -fr /var/log/messages-* /var/log/syslog.*',
                
                #'fdisk -l | grep sdb',
                #'cd /root/tools/medusa/image; rm -fr linux-x86*; scp /mnt/image/medusa/linux-x86_6.0.1.156759.tar.gz .; tar zxvf linux-x86_6.0.1.156759.tar.gz',
                'find ' + medusa_log_directory + ' -name *.bad -print',
                
                #'rpm -Uvh /mnt/image/driver/rhel/kmod-enic-2.1.1.83-rhel6u5.el6.x86_64.rpm; modprobe enic',
                
                #"/bin/rm /etc/sysconfig/network-scripts/ifcfg-eth4-tmp",
                #"sed -i 's/IPV6INIT=no/IPV6INIT=\\\"no\\\"/' /etc/sysconfig/network-scripts/ifcfg-eth4-tmp",
                #"echo IPADDR=\\\"20.3.25.$$host_suffix$$\\\" >> /etc/sysconfig/network-scripts/ifcfg-eth4-tmp",
                #"echo NETMASK=\\\"255.255.255.0\\\" >> /etc/sysconfig/network-scripts/ifcfg-eth4-tmp",
                "egrep -i '" + sp_define.PATTERN_ERROR_ONLY + "' /var/log/messages* /var/log/syslog* | grep -v real_update_permanent_hw_address | grep -v ERST | grep -v systemd-fsck | grep -v re-mounted | grep -v bluetooth | grep -v gdm-simple-slave",
                "egrep -i '" + sp_define.PATTERN_EGREP + "' " + medusa_log_directory + "*.log " + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                "egrep -i '" + sp_define.PATTERN_EGREP + "' " + medusa_log_directory + "*/*.log " + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                "egrep -i 'Data corruption detected' /root/tools/medusa/*/*/*.log",
                #"sed -i 's/loop=1/loop=10/' /root/tools/medusa/shell-sdb/define.sh",
                
                #"sed -i 's/-t3/-t6/' /root/tools/medusa/shell-sdb/medusa-all.sh",
                #"tar xvf tools.tar",
                #'grep -i error /mnt/$$host_suffix$$/tmp/messages* | grep -v real_update_permanent_hw_address | grep -v ERST',
                #'grep -i error /mnt/*/1*/*.log | ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                #'grep -i error /mnt/*/*.log | ' + sp_define.PATTERN_EXCLUSIVE_IN_MEDUSA,
                #'find /mnt -name *.bad -print',
                "cd /root/tools/iperf; /mnt/cmd/shell/iperf_server.sh",
                #stop rhel 7.0 firewall
                'service iptables stop', 
                "cd /root/tools/iperf; /mnt/cmd/shell/iperf_client.sh",
                
                "cd /root/tools/iperf; tail client*.log; sleep 5; tail client*.log",
                "killall iperf",
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
            except (pexpect.EOF):
                # for rhel 7.0 reboot cmd only
                if ip_suffix in [131, 132, 141, 142] and cmd == 'reboot':
                    print "Warning: Connection is closed"
                    result_dict[host_ip] = True
                else:
                    result_dict[host_ip] = False
            except (KeyboardInterrupt, AttributeError, pexpect.TIMEOUT):
                print "ERROR: Timeout"
                result_dict[host_ip] = False
            except:
                print "Unexpected error:", sys.exc_info()[0]
                result_dict[host_ip] = False
                
        print "\n\n\n"
        Util.print_host_status(result_dict)
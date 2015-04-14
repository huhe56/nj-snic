#!/usr/local/bin/python
'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    cmd = ' '.join(sys.argv[1:])
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        ip_suffix = Util.get_ip_field(host_ip, 3)
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
            if int(ip_suffix) in [131, 132, 141, 142] and cmd == 'reboot':
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
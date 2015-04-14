'''
Created on Aug 26, 2014

@author: huhe
'''

import sys, pexpect
from cmd.ucsm.server import sp_define
from lib.node_compute import NodeCompute
from lib.util import Util

if __name__ == '__main__':
    
    host_ip_list = sp_define.get_all_host_ip()
    result_dict = {}
    for host_ip in host_ip_list:
        if not host_ip in sp_define.HOST_LIST: continue
        print "\n"
        print '-'*30 + host_ip + '-'*30
        try:
            node = NodeCompute(host_ip)
            snic_version = node.get_snic_version()
            enic_version = node.get_enic_version()
            os_version = node.get_os_version()
            
            print '='*20 + "; " + snic_version + "; " + enic_version + "; "+ os_version
            node.exit()
            result_dict[host_ip] = '; '.join([os_version, snic_version, enic_version])
        except (KeyboardInterrupt, AttributeError, pexpect.TIMEOUT):
                print "ERROR: Timeout"
                result_dict[host_ip] = False
        except:
            print "Unexpected error:", sys.exc_info()[0]
            result_dict[host_ip] = False
            
    print "\n"
    Util.print_host_status(result_dict)
            
    
    
        
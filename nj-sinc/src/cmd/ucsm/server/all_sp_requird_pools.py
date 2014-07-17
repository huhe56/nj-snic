'''
Created on Aug 26, 2014

@author: huhe
'''


from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define


if __name__ == '__main__':
    
    param  = sp_define.param
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ucsm_ssh = ucsm.get_ssh()
    
    sp_define.create_boot_policy(ucsm_ssh, param)
    
    sp_define.create_kvm_console_ip_pool(ucsm_ssh, param)
    
    for raid_level, policy in sp_define.raid_level_disk_group_config_policy_dict.iteritems():
        param['tag_disk_group_config_policy_name'] = policy['policy_name']
        param['tag_raid_level'] = policy['policy_raid_level_name']
        sp_define.create_disk_group_config_policy(ucsm_ssh, param)
                
    ucsm.exit()
    

    
    
        
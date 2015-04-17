
import pprint

from main.define import Define
from lib.util import Util

from cmd.ucsm.server.sp_define_config_7 import config_dict

HOST_SUFFIXE_ALL_LIST = [111, 112, 121, 122, 151, 171]

HOST_SUFFIXE_LIST = [171]




HOST_LIST = ['20.200.10.' + str(host) for host in HOST_SUFFIXE_LIST]

MEDUSA_EXECUTION_ROOT = '/root'
MEDUSA_EXECUTION_ROOT = '/mnt'

'''
type = 1; boot lun
type = 2; data lun
type = 3; all lun
'''
MEDUSA_TEST_LUN_TYPE = 3

VLAN_PXE    = 20
VLAN_ISCSI  = 114
VLAN_MEDUSA = 2000

HOST_HYPERV_LIST = [121, 122, 171]
HOST_NEWARD_LIST = [151, 171]

PATTERN_EXCLUSIVE_IN_MEDUSA = '| grep -v label | grep -v "v Retry count on error" | grep -v "O loop error event handlers:" | grep -v "exit code 0" | grep -v "O Override base offset"'
PATTERN_EGREP = 'error|fail|halt|panic'
PATTERN_ERROR_ONLY = 'error'

mgmt_ip_pool_dict = {
    1:  {
        "tag_kvm_ip_start":    "10.193.221.134",
        "tag_kvm_ip_end":      "10.193.221.139",
        "tag_kvm_ip_gateway":  "10.193.221.254",
        "tag_kvm_ip_netmask":  "255.255.255.0",
        },
    3:  {
        "tag_kvm_ip_start":    "10.193.221.210",
        "tag_kvm_ip_end":      "10.193.221.225",
        "tag_kvm_ip_gateway":  "10.193.221.254",
        "tag_kvm_ip_netmask":  "255.255.255.0",
        }
    }


raid_level_disk_group_config_policy_dict = {
                   0: {'policy_name': 'raid0striped', 'policy_raid_level_name': 'raid-0-striped'},
                   1: {'policy_name': 'raid1mirrored', 'policy_raid_level_name': 'raid-1-mirrored'},
                   }

param = {
             "tag_boot_policy": "disk-pxe-uefi",
             "tag_boot_mode":   "legacy",
             
             "chassis_id":      None,
             "cartridge_id":    None,
             "server_id":       None,
             "tag_disk_size": "22000",
             
             
             # "tag_disk_group_config_policy_name": "raid0striped",
             # "tag_raid_level": "raid-0-striped",
             
             "tag_disk_group_config_policy_name": "raid1mirrored",
             "tag_raid_level": "raid-1-mirrored",
             
             
             "eth_pxe_name_prefix": "eth",
             "eth_pxe_name_index":   0,
             
             "tag_kvm_ip_pool_name":"kvm-console-ip-pool",
             "tag_kvm_ip_start":    "10.193.221.134",
             "tag_kvm_ip_end":      "10.193.221.139",
             "tag_kvm_ip_gateway":  "10.193.221.254",
             "tag_kvm_ip_netmask":  "255.255.255.0",

             "tag_mac_pool_name":   "snic_mac_pool",
             "tag_mac_start":       "00:25:B5:00:00:00",
             "tag_mac_end":         "00:25:B5:00:00:0F",
             
             "tag_eth_vlan":    "vlan10",
             "tag_eth_fabric":  "a",
             "tag_eth_order":   "1",
             
             # "mac_prefix":  '00:25',
             "uuid_prefix": '00000000-0000-0000-2601-000000'
    
             # ''' --------- auto generate ---------- '''
             # "tag_service_profile_name": "sp_1_3_2",
             # "tag_mac_address": "00:25:B5:01:03:02",
             # "tag_uuid":        "00000000-0000-0000-0000-000000010302",
             # "tag_local_lun":   "lun132",
             # "tag_volumn_name": "volumn132",
    }


test_bed = Define.TEST_BED
config = config_dict[test_bed]
param['test_bed_id'] = test_bed
param['tag_kvm_ip_start'] = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_start']
param['tag_kvm_ip_end'] = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_end']
param['tag_kvm_ip_gateway'] = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_gateway']
param['tag_kvm_ip_netmask'] = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_netmask']


def create_boot_policy(ucsm_ssh, param):
    
    param['tag_boot_policy'] = 'disk-pxe-legacy'
    param['tag_boot_mode'] = 'legacy'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_disk_pxe.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    param['tag_boot_policy'] = 'disk-pxe-uefi'
    param['tag_boot_mode'] = 'uefi'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_disk_pxe.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    param['tag_boot_policy'] = 'iscsi-pxe-legacy'
    param['tag_boot_mode'] = 'legacy'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_iscsi_pxe.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    param['tag_boot_policy'] = 'iscsi-pxe-uefi'
    param['tag_boot_mode'] = 'uefi'
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_iscsi_pxe.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_kvm_console_ip_pool(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "kvm_console_ip_pool.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_disk_group_config_policy(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "disk_group_config_policy.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_storage_profile(ucsm_ssh, param):
    
    #disk_policy_name = 'raid0striped'
    disk_policy_name = 'raid1mirrored'
    
    param['tag_storage_profile_name']   = 'sp-1-lun'
    param['tag_local_lun_name_1']       = 'sp1lun_1'
    param['tag_disk_policy_name_1']     = disk_policy_name
    param['tag_order_1']  = '1'
    param['tag_size_1']   = '50'
    param['cmd_text_file_name'] = 'storage_profile_1_lun.txt'
    run(ucsm_ssh, param)
    
    param['tag_storage_profile_name']   = 'sp-2-lun'
    param['tag_local_lun_name_1']       = 'sp2lun_1'
    param['tag_disk_policy_name_1']     = disk_policy_name
    param['tag_expand_to_avail_1']      = 'no'
    param['tag_order_1']  = '1'
    param['tag_size_1']   = '50'
    param['tag_local_lun_name_2']       = 'sp2lun_2'
    param['tag_disk_policy_name_2']     = disk_policy_name
    param['tag_order_2']  = '2'
    param['tag_size_2']   = '10'
    param['cmd_text_file_name'] = 'storage_profile_2_lun.txt'
    run(ucsm_ssh, param)
    
    param['tag_storage_profile_name']   = 'sp-4-lun'
    param['tag_local_lun_name_1']       = 'sp4lun_1'
    param['tag_disk_policy_name_1']     = disk_policy_name
    param['tag_expand_to_avail_1']      = 'no'
    param['tag_order_1']  = '1'
    param['tag_size_1']   = '50'
    param['tag_local_lun_name_2']       = 'sp4lun_2'
    param['tag_disk_policy_name_2']     = disk_policy_name
    param['tag_order_2']  = '2'
    param['tag_size_2']   = '200'
    param['tag_local_lun_name_3']       = 'sp4lun_3'
    param['tag_disk_policy_name_3']     = disk_policy_name
    param['tag_order_3']  = '3'
    param['tag_size_3']   = '6'
    param['tag_local_lun_name_4']       = 'sp4lun_4'
    param['tag_disk_policy_name_4']     = disk_policy_name
    param['tag_order_4']  = '4'
    param['tag_size_4']   = '8'
    param['cmd_text_file_name'] = 'storage_profile_4_lun.txt'
    run(ucsm_ssh, param)
    

def get_ip_list(start_ip, count):
    start_ip_item = start_ip.split('.')
    last_byte = int(start_ip_item[3])
    ip_list = []
    for i in range(count):
        start_ip_item[3] = str(last_byte)
        this_ip = '.'.join(start_ip_item)
        ip_list.append(this_ip)
        last_byte += 1
    return ip_list

    
def set_server_ext_mgmt_ip(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "server_ext_mgmt_ip.txt"   
    ip_list = get_ip_list(param['tag_kvm_ip_start'], 16)
    for chassis_id, chassis in config.iteritems():
        if chassis_id != 1: continue
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():
                param['tag_server_id']   = '/'.join([str(chassis_id), str(cartridge_id), str(server_id)])
                param['tag_addr']        = ip_list.pop()
                param['tag_default_gw']  = param['tag_kvm_ip_gateway']
                param['tag_subnet']      = param['tag_kvm_ip_netmask']
                Util.run_text_step(ucsm_ssh, file_text_step, param)

    
def create_service_profile(ucsm_ssh, param):
    test_bed    = str(param['test_bed_id'])
    chassis     = str(param['chassis_id'])
    cartridge   = str(param['cartridge_id'])
    server      = str(param['server_id'])
    
    chassis_id = str(chassis).zfill(2)
    cartridge_id = str(cartridge).zfill(2)
    server_id = str(server).zfill(2)
    
    server_full_id_list = [chassis_id, cartridge_id, server_id]
    server_full_id = ''.join(server_full_id_list)
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_uuid'] = ''.join([param['uuid_prefix'], server_full_id])
    
    # pprint.pprint(param)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    

def get_service_profile_name(chassis, cartridge, server):
    return 'sp-' + ''.join([chassis, cartridge, server]) 


def get_service_profile_name_from_param(param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    return get_service_profile_name(chassis, cartridge, server)


def get_mac_address(test_bed, chassis, cartridge, server, eth, vm='00'):
    mac = [None] * 6
    mac[0] = '00'
    mac[1] = '25'
    mac[2] = test_bed + chassis
    mac[3] = cartridge + server
    mac[4] = vm
    mac[5] = eth
    return ':'.join(mac)


def create_lun_in_service_profile(ucsm_ssh, param, lun):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    for lun_order, lun_detail in lun.iteritems():
        param['tag_lun_order'] = str(lun_order)
        param['tag_disk_size'] = str(lun_detail['disk_size'])
        raid_level = lun_detail['raid_level']
        param['tag_disk_group_config_policy_name'] = raid_level_disk_group_config_policy_dict[raid_level]['policy_name']
        param['tag_local_lun'] = ''.join(['lun', chassis, cartridge, server]) + '_' + str(lun_order)    
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_storage_lun.txt"   
        Util.run_text_step(ucsm_ssh, file_text_step, param)
        
        
def set_vnic_mtu_in_service_profile(ucsm_ssh, param, mtu_dict):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    for eth_name, mtu in mtu_dict.iteritems():
        param['tag_eth_name'] = eth_name
        param['tag_mtu'] = str(mtu)
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_vnic_mtu.txt"   
        Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def set_vnic_no_vlan_in_service_profile(ucsm_ssh, param, vlan_number_list):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    for vlan_number in vlan_number_list:
        param['tag_eth_name'] = 'eth' + str(vlan_number)
        param['tag_vlan_name'] = 'vlan' + str(vlan_number)
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_vnic_no_vlan.txt"   
        Util.run_text_step(ucsm_ssh, file_text_step, param)
        

def create_storage_profile_in_service_profile(ucsm_ssh, param, storage_profile):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_storage_profile_name'] = storage_profile
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_storage_profile.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_iscsi_in_service_profile(ucsm_ssh, param):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_iscsi.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)


def create_eth_if_in_service_profile(ucsm_ssh, param, eth_cnt):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    for eth_index in range(1, eth_cnt+1): 
        eth_id = str(eth_index).zfill(2) 
        param['tag_mac_address'] = get_mac_address(test_bed, chassis, cartridge, server, eth_id)
        param["tag_eth_name"] = ''.join([param["eth_pxe_name_prefix"], eth_id])
        param["tag_eth_vlan"] = 'default'
        param['tag_eth_order'] = eth_id
        if eth_index % 2 == 1:
            param["tag_eth_fabric"] = 'a'
        else:
            param["tag_eth_fabric"] = 'b'
        #pprint.pprint(param)
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_eth_vlan.txt"   
        Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def associate_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    server_full_list = [chassis, cartridge, server]
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_server_full_id'] = '/'.join(server_full_list)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_association.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def disassociate_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    server_full_list = [chassis, cartridge, server]
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_server_full_id'] = '/'.join(server_full_list)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_dis_association.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_ssh_sol_in_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    server_full_list = [chassis, cartridge, server]
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_server_full_id'] = '/'.join(server_full_list)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_ssh_sol.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_ipmi_in_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    server_full_list = [chassis, cartridge, server]
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_server_full_id'] = '/'.join(server_full_list)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_ipmi.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def delete_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_deletion.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def execute_cmd(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_deletion.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def remove_local_lun(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "local_lun_remove.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def reuse_local_lun(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "local_lun_reuse.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def power_cycle_service_profile(ucsm_ssh, param, wait=False):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_power_cycle_timing'] = 'immediate'
    if wait:
        param['tag_power_cycle_timing'] = 'wait'
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_power_cycle.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
    
def change_boot_policy_order(ucsm_ssh, param, order_storage_local_any=1, order_lan=2):
    param['tag_boot_storage_local_any_order'] = str(order_storage_local_any)
    param['tag_boot_lan_order'] = str(order_lan)

    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "boot_policy_order_change.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def run(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + param['cmd_text_file_name']   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def run_in_service_profile(ucsm_ssh, param):
    param['tag_service_profile_name'] = get_service_profile_name_from_param(param)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "local_lun_reuse.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def get_all_host_ip():
    host_ip_prefix = '20.200.10.'
    host_ip_list = []
    for chassis_id, chassis in config.iteritems():
        for cartridge_id, cartridge in chassis.iteritems():
            for server_id, server in cartridge.iteritems():    
                host_ip_list.append(host_ip_prefix + str(chassis_id) + str(cartridge_id) + str(server_id))
    return host_ip_list


def create_mac_pool(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "mac_pool.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_ipmi_policy(ucsm_ssh, param):
    file_json_step = Define.PATH_SNIC_JSON_UCSM + "ipmi_policy.json"   
    Util.run_step_list(ucsm_ssh, file_json_step)
    

def vnic_add_vlan_in_service_profile(ucsm_ssh, param):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    host_suffix = int(''.join([chassis, cartridge, server]))
    eth_cnt = 16 if host_suffix in HOST_NEWARD_LIST else 8
    is_hyperv = True if host_suffix in HOST_HYPERV_LIST else False
    
    ucsm_ssh.send_expect_prompt('scope org')
    ucsm_ssh.send_expect_prompt('scope service-profile ' + param['tag_service_profile_name'])
    
    if is_hyperv:
        # mgmt
        for eth_id in range(2, eth_cnt/2+1):
            vnic_add_vlan_for_hyperv(ucsm_ssh, True, eth_id)
        # vm
        for eth_id in range(eth_cnt/2+1, eth_cnt+1):
            vnic_add_vlan_for_hyperv(ucsm_ssh, False, eth_id)
    else:
        vnic_add_vlan_for_standalone(ucsm_ssh, eth_cnt)
    ucsm_ssh.send_expect_prompt("commit-buffer")
        
        
def vnic_add_vlan_for_hyperv(ucsm_ssh, is_mgmt, eth_id):
    eth_name = 'eth' + str(eth_id).zfill(2)
    ucsm_ssh.send_expect_prompt('scope vnic ' + eth_name)
    vlan_list = Define.VLAN_MGMT if is_mgmt else Define.VLAN_VM
    for vlan in vlan_list:
        ucsm_ssh.send_expect_prompt('enter eth-if vlan' + str(vlan))
        ucsm_ssh.send_expect_prompt('exit')
    ucsm_ssh.send_expect_prompt('exit')
        
        
def vnic_add_vlan_for_standalone(ucsm_ssh, eth_cnt):
    vlan_list = Define.VLAN_STANDALONE
    len_diff = eth_cnt - len(vlan_list)
    vlan_list_padded = [ 100 + x for x in range(1, len_diff+1)]
    vlan_list = vlan_list + vlan_list_padded  
    for eth_id in range(1, eth_cnt+1):
        eth_name = 'eth' + str(eth_id).zfill(2)
        ucsm_ssh.send_expect_prompt('scope vnic ' + eth_name)
        vlan = vlan_list.pop(0)
        ucsm_ssh.send_expect_prompt('enter eth-if vlan' + str(vlan))
        ucsm_ssh.send_expect_prompt('set default-net yes')
        ucsm_ssh.send_expect_prompt('exit')
        ucsm_ssh.send_expect_prompt('delete eth-if default')
        ucsm_ssh.send_expect_prompt('exit')
    
    
        
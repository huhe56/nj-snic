
import pprint

from main.define import Define
from lib.util import Util

config_dict = {
    1: {
        1: {
            3: {
                1:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 40000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                },
            4: {
                1:    {'disk_size': 60000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 100000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                }
            }
        },
    3: {
        1: {
            1: {
                1:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                  },
            2: {
                1:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                  },
            3: {
                1:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                  },
            4: {
                1:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                2:    {'disk_size': 20000, 'raid_level': 1, 'boot_policy': 'uefi', 'eth_cnt': 4},
                },
            }
        }
    }

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
             
             "chassis_id":      1,
             "cartridge_id":    4,
             "server_id":       2,
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
             
             #"mac_prefix":  '00:25',
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
param['tag_kvm_ip_start']   = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_start']
param['tag_kvm_ip_end']     = mgmt_ip_pool_dict[test_bed]['tag_kvm_ip_end']
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
    
    
def create_kvm_console_ip_pool(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "kvm_console_ip_pool.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_disk_group_config_policy(ucsm_ssh, param):
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "disk_group_config_policy.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    
    
def create_service_profile(ucsm_ssh, param):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    chassis_id = str(chassis).zfill(2)
    cartridge_id = str(cartridge).zfill(2)
    server_id = str(server).zfill(2)
    eth_id = str(param['eth_pxe_name_index']).zfill(2)
    
    server_full_id_list = [chassis_id, cartridge_id, server_id]
    server_full_id = ''.join(server_full_id_list)
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    param['tag_local_lun'] = ''.join(['lun', server_full_id])
    param['tag_volumn_name'] = ''.join(['volumn', server_full_id])
    param['tag_mac_address'] = get_mac_address(test_bed, chassis, cartridge, server, eth_id)
    param["tag_eth_name"] = ''.join([param["eth_pxe_name_prefix"], str(param["eth_pxe_name_index"])])
    param['tag_uuid'] = ''.join([param['uuid_prefix'], server_full_id])
    
    # pprint.pprint(param)
    
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile.txt"   
    Util.run_text_step(ucsm_ssh, file_text_step, param)
    

def get_service_profile_name(chassis, cartridge, server):
    return 'sp-' + ''.join([chassis, cartridge, server]) 


def get_mac_address(test_bed, chassis, cartridge, server, eth, vm='00'):
    mac = [None]*6
    mac[0] = '00'
    mac[1] = '25'
    mac[2] = test_bed + chassis
    mac[3] = cartridge + server
    mac[4] = vm
    mac[5] = eth
    return ':'.join(mac)


def create_eth_if_in_service_profile(ucsm_ssh, param, eth_cnt):
    test_bed = str(param['test_bed_id'])
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    eth_id = str(param['eth_pxe_name_index']).zfill(2)
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    
    current_eth_cnt = 0
    eth_id_number_list = range(3, 8)
    eth_id_number_list.insert(0, 113)
    eth_id_number_list.insert(0, 2000)
    for eth_id_number in eth_id_number_list: 
        eth_id = str(eth_id_number).zfill(2)
        if eth_id_number == 113:
            eth_id = '02'
        elif eth_id_number == 2000:
            eth_id = '01'
        vlan_id = str(120 + eth_id_number)
        if eth_id_number == 113 or eth_id_number == 2000:
            vlan_id = str(eth_id_number)
        param['tag_mac_address'] = get_mac_address(test_bed, chassis, cartridge, server, eth_id)
        param["tag_eth_name"] = ''.join([param["eth_pxe_name_prefix"], vlan_id])
        param["tag_eth_vlan"] = ''.join(["vlan", vlan_id])
        param['tag_eth_order'] = str(int(eth_id) + 1)
        if eth_id_number == 2000:
            param["tag_eth_fabric"] = 'b'
        elif eth_id_number == 113:
            param["tag_eth_fabric"] = 'a'
        elif eth_id_number % 2 == 1:
            param["tag_eth_fabric"] = 'b'
        else:
            param["tag_eth_fabric"] = 'a'
        pprint.pprint(param)
        file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_eth_vlan.txt"   
        Util.run_text_step(ucsm_ssh, file_text_step, param)
        current_eth_cnt += 1
        if current_eth_cnt >= eth_cnt: 
            break
    
    
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
    
    
def delete_service_profile(ucsm_ssh, param):
    chassis = str(param['chassis_id'])
    cartridge = str(param['cartridge_id'])
    server = str(param['server_id'])
    
    param['tag_service_profile_name'] = get_service_profile_name(chassis, cartridge, server)
    file_text_step = Define.PATH_SNIC_TEXT_UCSM + "service_profile_deletion.txt"   
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
    
    
                

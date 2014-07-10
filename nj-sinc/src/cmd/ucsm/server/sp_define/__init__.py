
param = {
             "chassis_id":      1,
             "cartridge_id":    5,
             "server_id":       1,
             "tag_disk_size": "16000",
             
             "eth_pxe_name_prefix": "eth",
             "eth_pxe_name_index":   0,
             
             "tag_kvm_ip_pool_name":"kvm-console-ip-pool",
             "tag_kvm_ip_start":    "10.193.221.134",
             "tag_kvm_ip_end":      "10.193.221.139",
             "tag_kvm_ip_gateway":  "10.193.221.254",
             "tag_kvm_ip_netmask":  "255.255.255.0",

             "tag_boot_policy": "bp-disk-pxe",

             "tag_disk_group_config_policy_name": "raid0striped",
             "tag_raid_level": "raid-0-striped",
             
             "tag_eth_vlan":    "vlan10",
             "tag_eth_fabric":  "a",
             "tag_eth_order":   "1",
             
             "mac_prefix":  '00:25',
             "uuid_prefix": '00000000-0000-0000-2601-000000'
    
             #''' --------- auto generate ---------- '''
             #"tag_service_profile_name": "sp_1_3_2",
             #"tag_mac_address": "00:25:B5:01:03:02",
             #"tag_uuid":        "00000000-0000-0000-0000-000000010302",
             #"tag_local_lun":   "lun132",
             #"tag_volumn_name": "volumn132",
    }

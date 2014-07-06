
param = {
             "chassis_id":      1,
             "cartridge_id":    4,
             "server_id":       2,
             "tag_mgmt_ip_address": "10.193.221.136",
             "tag_disk_size": "20000",
             
             
             "eth_pxe_name_prefix": "eth",
             "eth_pxe_name_index":   0,
             
             "tag_mgmt_ip_gateway": "10.193.221.254",
             "tag_mgmt_ip_netmask": "255.255.255.0",

             "tag_boot_policy": "bp-disk-pxe",

             "tag_disk_group_config_policy_name": "raid0striped",
             
             "tag_eth_vlan":    "vlan10",
             "tag_eth_fabric":  "a",
             
             "mac_prefix":  '00:25',
             "uuid_prefix": '00000000-0000-0000-2601-000000'
    
             #''' --------- auto generate ---------- '''
             #"tag_service_profile_name": "sp_1_3_2",
             #"tag_mac_address": "00:25:B5:01:03:02",
             #"tag_uuid":        "00000000-0000-0000-0000-000000010302",
             #"tag_local_lun":   "lun132",
             #"tag_volumn_name": "volumn132",
    }
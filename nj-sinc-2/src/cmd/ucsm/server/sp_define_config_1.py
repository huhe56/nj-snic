'''
Created on Sep 25, 2014

@author: huhe
'''

RAID_LEVEL_0    = 0
RAID_LEVEL_1    = 1
raid_level = RAID_LEVEL_0

LUN_SIZE_1  = 40
LUN_SIZE_2  = 20

config_dict = {
    # test bed 3
    3: {
        # chassis 1
        1: { 
            1: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
            },
            2: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
            },
            3: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
            },
            4: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            },
            5: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            },
            6: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            },
            7: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            },
            8: {
                1: {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                        },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'lun': {
                            1: {'disk_size': LUN_SIZE_1, 'raid_level': raid_level},
                            2: {'disk_size': LUN_SIZE_2, 'raid_level': raid_level},
                            },
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            }
        },
        # for reuse test purpose, still use chassis servers
        2: {
            4: {
                1: {
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            },
            5: {
                1: {
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                },
                2:  {
                       'boot_policy': 'uefi',
                       'eth_cnt': 4
                }
            }
        }
    }
}

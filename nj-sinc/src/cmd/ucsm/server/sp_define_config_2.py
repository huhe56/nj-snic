'''
Created on Sep 25, 2014

@author: huhe
'''

SP_1_LUN    = 'sp-1-lun'
SP_2_LUN    = 'sp-2-lun'

SP_NAME_1   = SP_1_LUN
SP_NAME_2   = SP_2_LUN

BOOT_POLICY_LEGACY  = 'legacy'
BOOT_POLICY_UEFI    = 'uefi'

BOOT_POLICY_1   = BOOT_POLICY_UEFI
BOOT_POLICY_2   = BOOT_POLICY_UEFI

config_dict = {
    # test bed 3
    3: {
        # chassis 1
        1: { 
            1: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                },
            },
            2: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                },
            },
            3: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                },
            },
            4: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            },
            5: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            },
            6: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            },
            7: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            },
            8: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            }
        },
        # for reuse test purpose, still use chassis servers
        2: {
            4: {
                1: {
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            },
            5: {
                1: {
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': 4
                },
                2:  {
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': 4
                }
            }
        }
    }
}

'''
Created on Sep 25, 2014

@author: huhe
'''

SP_1_LUN    = 'sp-1-lun'
SP_2_LUN    = 'sp-2-lun'

SP_NAME_1   = SP_1_LUN
SP_NAME_2   = SP_1_LUN

BOOT_POLICY_LEGACY  = 'disk-pxe-legacy'
BOOT_POLICY_UEFI    = 'disk-pxe-uefi'

BOOT_POLICY_1   = BOOT_POLICY_LEGACY
BOOT_POLICY_2   = BOOT_POLICY_UEFI

ETH_CNT = 8

config_dict = {
    # test bed 3
    3: {
        # chassis 1
        1: { 
            1: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                },
            },
            2: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                },
            },
            3: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2: {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                },
            },
            4: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                }
            },
            5: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                }
            },
            6: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                }
            },
            7: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                }
            },
            8: {
                1: {
                       'storage_profile': SP_NAME_1,
                       'boot_policy': BOOT_POLICY_1,
                       'eth_cnt': ETH_CNT
                },
                2:  {
                       'storage_profile': SP_NAME_2,
                       'boot_policy': BOOT_POLICY_2,
                       'eth_cnt': ETH_CNT
                }
            }
        }
    }
}

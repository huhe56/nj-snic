'''
Created on Aug 15, 2013

@author: huhe
'''

PEXPECT_OUTPUT_STDOUT   = True
HOST_IP = None

class Define():
    '''
    classdocs
    '''
    
    TEST_BED = 3
    
    UCSM_BUNDLE_LATEST_BUILD_NUMBER     = 65
    UCSM_BUNDLE_LATEST_BUILD_REVISION   = "140909-143109-rev189149-65"
    
    UCSM_HOSTNAME   = None
    UCSM_HOSTNAME_B = None
    NJ_HOSTNAME     = None
    NODE_DEFAULT_USERNAME   = None
    PATH_DOWNLOADS  = None
    
    if TEST_BED == 1:
        UCSM_HOSTNAME   = "10.193.221.130"
        UCSM_HOSTNAME_B = "10.193.221.132"
        NJ_HOSTNAME     = "10.193.221.133"
        NODE_DEFAULT_USERNAME   = 'huhe'
    elif TEST_BED == 3:
        UCSM_HOSTNAME   = "10.193.221.150"
        UCSM_HOSTNAME_B = "10.193.221.152"
        NJ_HOSTNAME     = "10.193.221.153"
        NODE_DEFAULT_USERNAME   = 'huan'
    
    NODE_HEAD_NAME          = "10.193.221.245"
    NODE_USERNAME_ROOT      = 'root'
    NODE_DEFAULT_PASSWORD   = 'huanhe56'
    
    SERVER_DEFAULT_PASSWORD = 'nbv12345'
    
    PATH_DOWNLOADS          = "/tmp"
    
    PATH_NJ_ROOT            = "/home/huhe/workspace/nj/"
    PATH_SNIC_ROOT          = PATH_NJ_ROOT + "snic/"
    
    PATH_SNIC_SRC          = PATH_SNIC_ROOT + "src/"
    PATH_SNIC_CMD_DEFINE   = PATH_SNIC_SRC + "cmd_define/"
    
    PATH_SNIC_JSON         = PATH_SNIC_CMD_DEFINE + "json/"
    PATH_SNIC_JSON_LINUX   = PATH_SNIC_JSON + "linux/"
    PATH_SNIC_JSON_UCSM    = PATH_SNIC_JSON + "ucsm/"
    PATH_SNIC_JSON_NJ      = PATH_SNIC_JSON + "nj/"
    
    PATH_SNIC_TEXT         = PATH_SNIC_CMD_DEFINE + "text/"
    PATH_SNIC_TEXT_UCSM    = PATH_SNIC_TEXT + "ucsm/"
    
    PATH_SNIC_CONFIG       = PATH_SNIC_ROOT + "config/"
    PATH_SNIC_LOG          = PATH_SNIC_ROOT + "log/"
    PATH_SNIC_LOG_FILE     = PATH_SNIC_LOG + "pexpect.log"
    PATH_SNIC_LOG_FILE_ALL = PATH_SNIC_LOG + "all.log"
    PATH_SNIC_LOG_FILE_CONSOLE = PATH_SNIC_LOG + "console.log"

    
    DEVICE_DEFAULT_USERNAME = 'admin'
    DEVICE_DEFAULT_PASSWORD = 'passsword'
    
    UCSM_DEFAULT_USERNAME   = 'admin'
    UCSM_DEFAULT_PASSWORD   = 'nbv12345'

    TIMEOUT_SSH         = 20
    PATTERN_SSH_NEW_KEY = '(?i)are you sure you want to continue connecting'
    PATTERN_PASSWORD    = '(?i)password'
    PATTERN_PROMPT      = '[#$]'
    
    TIMEOUT_COMMIT = 60
    
    PATTERN_NEW_LINE    = "\r\n"

    SNIC_STATS_ERROR_LIST = [
                             'IOs Failed',
                             'IOs Not Found',
                             'Memory Alloc Failures',
                             'REQs Null',
                             'SCSI Cmd Pointers Null',
                             'Aborts',
                             'Aborts Fail',
                             'Aborts Timeout',
                             'FW Out Of Resource Errs',
                             'FW IO Errors',
                             'FW SCSI Errors',
                             'Data Count Mismatch',
                             'IOs w/ Timeout Status',
                             'IOs w/ Aborted Status',
                             'IOs w/ SGL Invalid Stat',
                             'WQ Desc Alloc Fail',
                             'Queue Full',
                             'Target Not Ready',
                             ]
    
    
    UCSM_BLADE_SERVER_LIST  = { 1: {
                                    1: "Blade1_node01", 
                                    2: "Blade2_node02", 
                                    3: "Blade3_node03",
                                    4: "Blade4_node04", 
                                    5: "Blade5_node05", 
                                    7: "Blade7_node06"
                                    }
                               }
    UCSM_RACK_SERVER_LIST   = {
                               1: "Rack-01_node07", 
                               2: "Rack-02_node08", 
                               3: "Rack-03_node09", 
                               4: "Rack-04_node10"
                               }
    
    
    URL_IMAGE_BUILD_ROOT = "http://savbu-swucs-bld3.cisco.com/elcapitan_ms-builds/"
    URL_IMAGE_LATEST_BUILD_ROOT = URL_IMAGE_BUILD_ROOT + UCSM_BUNDLE_LATEST_BUILD_REVISION + "/Images." + str(UCSM_BUNDLE_LATEST_BUILD_NUMBER) + "/"
    IMAGE_LIST = [
                  "ucs-k9-bundle-infra.2.5.0." + str(UCSM_BUNDLE_LATEST_BUILD_NUMBER) + ".A.gbin",
                  "ucs-k9-bundle-m-series.2.5.0." + str(UCSM_BUNDLE_LATEST_BUILD_NUMBER) + ".M.gbin"
                  ]
    URL_IMAGE_LIST = [URL_IMAGE_LATEST_BUILD_ROOT + image for image in IMAGE_LIST]
    
    
    CMD_SCP_IMAGE_ROOT = "scp://" + NODE_DEFAULT_USERNAME + "@" + NODE_HEAD_NAME + "/" + PATH_DOWNLOADS + "/"
    CMD_SCP_IMAGE_LIST = [CMD_SCP_IMAGE_ROOT + image for image in IMAGE_LIST ]
    
    CDEST_HUHE_PASSWORD = "he100he"
    URL_NODE_CDETS_TECH_SUPPORT = "huhe@10.193.175.2:/net/savbu-da01/qa/cdets/huhe/temp-tech-support"
    URL_UCSM_CDETS_TECH_SUPPORT = "scp://huhe@10.193.175.2/net/savbu-da01/qa/cdets/huhe/temp-tech-support"
    
    
    VNIC_POLICY_TYPE_QOS                = "qos-policy"
    VNIC_POLICY_TYPE_QOS_LABEL          = "qos"
    VNIC_POLICY_NAME_QOS_BEST_EFFORT    = "BestEffort-1500"
    VNIC_POLICY_NAME_QOS_PLATINUM       = "Platinum-9216"
    
    VNIC_MTU        = "mtu"
    VNIC_MTU_LABEL  = "mtu"
    
    HOST_DRIVER_1   = "node101"
    HOST_DRIVER_2   = "node103"
    
    MPI_HOST        = "--host"
    MPI_NP          = "-np"
    MPI_MCA         = "--mca btl usnic,sm,self"
    MPI_PATH        = "/home/huhe/ompi-tests/imb/src/IMB-MPI1"
    
    MPI_CMD_PINGPOND    = "pingpong"
    
    
    
    
    
    
'''
Created on Aug 26, 2013

@author: huhe
'''

import time

from main.define import Define
from lib.util import Util
from lib.node_head import NodeHead
from lib.ucsm import UCSM


if __name__ == '__main__':
    
    download = False
    
    if download:
        head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
        file_json_step = Define.PATH_SNIC_JSON_LINUX + "wget_ucsm_firmware.json"   
        Util.run_step_list(head_node.get_ssh(), file_json_step)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ssh = ucsm.get_ssh()
    
    for i in range(len(Define.IMAGE_LIST)):
        ssh.send_expect_prompt("top")
        ssh.send_expect_prompt("scope firmware")
        ssh.send("download image " + Define.CMD_SCP_IMAGE_LIST[i])
        ssh.expect(Define.PATTERN_PASSWORD)
        ssh.send_expect_prompt(Define.NODE_DEFAULT_PASSWORD)
        ssh.send_expect_prompt("scope download-task " + Define.IMAGE_LIST[i])
        ret = Util.probe_send_expect(ssh, "show", "Downloaded", 60, 10)
        if not ret: exit()    
    
    ssh.send_expect_prompt("top")
    ssh.send_expect_prompt("scope firmware")
    ssh.send_expect_prompt("scope auto-install")
    ssh.send("install infra infra-vers 2.5(1." + str(Define.UCSM_BUNDLE_LATEST_BUILD_NUMBER) + ")A")
    ssh.expect("yes\/no\):")
    ssh.send_expect_prompt("yes")
    ssh.exit()
    
    time.sleep(300)
    
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    ssh = ucsm.get_ssh()
    
    ssh.send_expect_prompt("top")
    ssh.send_expect_prompt("scope firmware")
    ssh.send_expect_prompt("scope auto-install")
    ret = Util.probe_send_expect(ssh, "show", "Pending User Ack", 300, 12)
    if not ret: exit()
    
    ssh.send_expect_prompt("acknowledge primary fabric-interconnect reboot")
    ssh.send_expect_prompt("commit-buffer")
    ssh.exit()
    
    time.sleep(300)
    
    ssh = Util.wait_for_node_to_boot_up(Define.UCSM_HOSTNAME_B, Define.UCSM_DEFAULT_USERNAME, Define.UCSM_DEFAULT_PASSWORD, "show version")
    ssh.exit()
    
    
        
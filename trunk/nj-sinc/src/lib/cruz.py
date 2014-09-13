
import time
import pexpect
from main.define import Define
from lib.util import Util
from lib.node_head import NodeHead

class Cruz:
    
    def __init__(self, cmc_ip=None):
        self._ssh = None
        
        head_node = NodeHead(Define.NODE_HEAD_NAME, Define.NODE_DEFAULT_USERNAME)
        self._ssh = head_node.get_ssh()
        self._ssh.send('cruz.sh')
        self._ssh.expect('Escape char is')
        self._ssh.send_expect_prompt('')
        
        
    def exit(self):
        self._ssh.send_control('x')
        
        
    def run_cmd_step(self, file_json_step):
        try:
            Util.run_step_list(self._ssh, file_json_step)
        except:
            self.exit()
            
            
    def wait_for_erase_complete(self, drive_id_list, sleep=None):
        self._ssh.send('storelibtest')
        self._ssh.expect('Please enter choice : ')
        self._ssh.send('4')
        self._ssh.expect('Please enter choice :')
        
        completed_count = 0
        while completed_count < len(drive_id_list):
            completed_count = 0
            for drive_id in drive_id_list:
                self._ssh.send('8')
                self._ssh.expect('Enter Device ID--->')
                self._ssh.send(str(drive_id))
                ret = self._ssh.expect([pexpect.TIMEOUT, 'Erase in progress'], 2)
                if ret == 0:
                    completed_count += 1
                time.sleep(1)
                self._ssh.send('')
            if sleep:
                time.sleep(sleep)
        self._ssh.expect('Please enter choice :')
        self._ssh.send('0')
            
            
        
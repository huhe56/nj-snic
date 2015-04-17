

from lib.util import Util
from lib.ssh import SSH

class RAR:
    
    def __init__(self, hostname, username, password):        
        self._ssh = SSH(hostname, username, password)
        
        
    def exit(self):
        self._ssh.send_expect_prompt('exit')
        
    
    def power_cycle(self, outlet_id):
        self._ssh.send_expect_prompt('power outlets ' + str(outlet_id) + ' cycle /y')
        
        
    def run_cmd_step(self, file_json_step):
        Util.run_step_list(self._ssh, file_json_step)
        

        
        
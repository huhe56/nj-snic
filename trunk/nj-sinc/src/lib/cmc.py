

from main.define import Define
from lib.util import Util
from lib.node_head import NodeHead

class CMC:
    
    
    
    def __init__(self, cmc_ip=None):
        self._ssh = None
        
        head_node = NodeHead('10.193.221.245', "huhe")
        self._ssh = head_node.get_ssh()
        self._ssh.send_expect_prompt('cmc.sh')
        
        
    def exit(self):
        self._ssh.send_expect_prompt('exit')
        
        
    def run_cmd_step(self, file_json_step):
        Util.run_step_list(self._ssh, file_json_step)
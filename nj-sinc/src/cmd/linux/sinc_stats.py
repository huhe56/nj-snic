'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.node_compute import NodeCompute


if __name__ == '__main__':
    
    node = NodeCompute('20.200.10.141')
    node.get_snic_stats()
    node.exit()
    
    
        
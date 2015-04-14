'''
Created on Aug 26, 2014

@author: huhe
'''

from main.define import Define
from lib.ucsm import UCSM
from cmd.ucsm.server import sp_define

'''
    enter eth-policy tag_eth_policy_name
        commit-buffer
        
        set trans-queue count             tag_trans_queue_count
        set trans-queue ring-size         tag_trans_queue_ring_size
        set recv-queue count              tag_recv_queue_count
        set recv-queue ring-szie          tag_recv_queue_ring_size
        set comp-queue count              tag_comp_queue_count
        
        set set_failback_timeout          tag_failback_timeout
        set interrupt_count               tag_interrupt_count
        set interrupt_coalescing_time     tag_interrupt_coalescing_time
        commit-buffer
'''

if __name__ == '__main__':
    
    param = sp_define.param
    ucsm = UCSM(Define.UCSM_HOSTNAME);
    
    ''' default '''
    
    param['tag_eth_policy_name']        = 'LNX-NJ-default'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 1
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 256
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 1
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 512
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 2
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 4
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = 5
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = 125
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ''' upper limit '''
    
    param['tag_eth_policy_name']        = 'LNX-NJ-upper'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 256
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 4096
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 256
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 4096
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 512
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 514
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = 600
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = 65535
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ''' lower limit '''
    param['tag_eth_policy_name']        = 'LNX-NJ-lower'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 1
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 64
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 1
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 64
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 1
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 1
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = 0
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = 0
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ''' random '''
    
    param['tag_eth_policy_name']        = 'LNX-NJ-middle'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 128
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 2048
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 128
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 2048
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 256
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 257
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = 300
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = 32767
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ucsm.exit()
    

    
    
        
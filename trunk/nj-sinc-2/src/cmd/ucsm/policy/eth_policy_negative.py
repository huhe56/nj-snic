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
    
    
    ''' upper limit '''
    
    param['tag_eth_policy_name']        = 'LNX-NJ-upper-nag'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 257
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 4097
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 257
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 4097
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 513
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 515
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = 601
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = 65536
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ''' lower limit '''
    param['tag_eth_policy_name']        = 'LNX-NJ-lower-nag'
    ''' 1 - 256 '''
    param['tag_trans_queue_count']      = 0
    ''' 64 - 4096 '''
    param['tag_trans_queue_ring_size']  = 63
    ''' 1 - 256 '''
    param['tag_recv_queue_count']       = 0
    ''' 64 - 4096 '''
    param['tag_recv_queue_ring_size']   = 63
    ''' 1 - 512 '''
    param['tag_comp_queue_count']       = 0
    ''' 1 - 514 '''
    param['tag_interrupt_count']        = 0
    ''' 0 - 600 '''
    param['tag_failback_timeout']       = -1
    ''' 0 - 65535 '''
    param['tag_interrupt_coalescing_time']   = -1
    param['cmd_text_file_name'] = 'eth_policy.txt'
    sp_define.run(ucsm.get_ssh(), param)
    
    ucsm.exit()
    

    
    
        
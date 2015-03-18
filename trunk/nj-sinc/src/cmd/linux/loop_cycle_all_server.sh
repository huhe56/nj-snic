#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "====================================*************** $i ***************===================================="
        echo ""
        date
        echo ""

        # reboot
        python ../ucsm/server/all_sp_power_cycle_wait.py
        sleep 120

        # check dmesg
        python execute_shell_cmd.py 2

        # check lun
        python execute_shell_cmd.py 3

        # sync up ntp server
        python execute_shell_cmd.py 4

        # restart network service
        # python execute_shell_cmd.py 5

        # mount data lun
        python execute_shell_cmd.py 6

        # firewall
        python execute_shell_cmd.py 9

        python iperf_start.py server
        python iperf_start.py client

        python medusa_start.py

        # check medusa and iperf process
        python execute_shell_cmd.py 8
        python execute_shell_cmd.py 7

        sleep 120
    done

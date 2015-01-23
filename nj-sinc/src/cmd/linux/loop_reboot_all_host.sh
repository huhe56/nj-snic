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
        python execute_shell_cmd.py 1
        sleep 900

        # check dmesg
        python execute_shell_cmd.py 2

        # check lun
        python execute_shell_cmd.py 3

        # sync up ntp server
        python execute_shell_cmd.py 4

        # restart network service
        python execute_shell_cmd.py 5

        # mount data lun
        python execute_shell_cmd.py 6

        python medusa_start.py
        python iperf_start.py server
        python iperf_start.py client

        # check medusa and iperf process
        python execute_shell_cmd.py 7
        python execute_shell_cmd.py 8

        sleep 300
    done

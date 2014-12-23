#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "===============*************** $i ***************==============="
        echo ""
        date
        echo ""
        python medusa_start.py
        python iperf_start.py server
        python iperf_start.py client
        sleep 300
        python ../ucsm/server/all_sp_power_cycle_wait.py
        sleep 900
    done


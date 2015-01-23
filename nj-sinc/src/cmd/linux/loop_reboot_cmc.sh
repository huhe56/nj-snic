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
        python reboot_cmc.py
        #sleep 900
        #python medusa_start.py
        #python iperf_start.py server
        #python iperf_start.py client
        sleep 1800
    done


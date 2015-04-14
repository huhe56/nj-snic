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
        sleep 600
    done


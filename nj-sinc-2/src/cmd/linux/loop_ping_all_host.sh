#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "===============--------------- $i ---------------==============="
        echo ""
        date
        python ping_all_hosts.py
        sleep 120
    done


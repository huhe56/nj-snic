#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "===============--------------- $i ---------------==============="
        echo ""
        date
        sleep 400
        python ping_all_hosts.py
    done

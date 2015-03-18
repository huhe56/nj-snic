#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "===============--------------- $i ---------------==============="
        echo ""
        date
        python get_uptime.py 
        python get_version.py 
        sleep 400
    done


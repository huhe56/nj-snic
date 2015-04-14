#!/bin/sh

while :
    do
        i=$(($i+1))
        echo ""
        echo ""
        echo "===============--------------- $i ---------------==============="
        echo ""
        date
        python run_shell_cmd.py dstat 5 2
        sleep 600
    done


#!/bin/sh

# set the host list to 1 host in sp_define.py

while :
    do
        i=$(($i+1))
        echo "=============== $i ==============="
        date
        python execute_shell_cmd.py 1
        sleep 120
    done


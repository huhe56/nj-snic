#!/bin/sh

while :
    do
        i=$(($i+1))
        echo "=============== $i ==============="
        date
        python stop_medusa_if_error.py
        sleep 1800
    done


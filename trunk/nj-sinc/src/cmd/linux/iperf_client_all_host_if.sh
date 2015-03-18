#!/bin/sh 

# /mnt/cmd/bin/iperf -c 20.200.10.171 -i 1 -t 360000

time=1200

subnet_list="20.200.10. 192.168.0. 20.3.23. 20.3.24. 20.3.25. 20.3.26. 20.3.27."
#subnet_list="20.3.26. 20.3.27."

i=1
for chassis in 1
    do
    for cartridge in 1 2 3 4 5 6 7 8
        do
        for server in 1 2
        do
            id="$chassis$cartridge$server"
            for subnet in $subnet_list
            do
                ip="$subnet$id"
                cmd="/usr/bin/iperf -c $ip -i 1 -t $time" 
                echo "$i $cmd"
                i=$(($i+1))
                $cmd &> client-$ip.log &
            done
        done
    done
done

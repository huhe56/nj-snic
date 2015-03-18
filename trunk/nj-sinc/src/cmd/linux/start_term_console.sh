#!/bin/bash 

for chassis in 1
do
    for cartridge in 1 2 3 4 5 6 7 8
    do
        for server in 1 2
        do
            host_id="$chassis$cartridge$server"
            desktop_id=$cartridge
            x=$((((server - 1)) * 300 + 444400))
            y=200
            gnome-terminal --title=$host_id -x sh -c "ssh_sol.sh $host_id"; wmctrl -r :ACTIVE: -t $desktop_id; wmctrl -r :ACTIVE: -e "1,$x,$y,-1,-1" 
        done
    done
done


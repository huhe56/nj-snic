#!/bin/sh

for chassis in 1
do
	for cartridge in 1 2 3 4 5 6 7 8
	do
		for server in 1 2
		do
			id="$chassis$cartridge$server"
			host_ip="20.200.10.$id"
            cmd="scp /tmp/kmod-snic-0.0.1.14-rhel6.5-1.el6.x86_64.rpm root@$host_ip:/tmp"
			echo $cmd
			$cmd
		done
	done
done
			

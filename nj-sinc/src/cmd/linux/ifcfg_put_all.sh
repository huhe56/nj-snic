#!/bin/sh

source_root_dir="/home/huhe/nj/ifcfg"

for chassis in 1
do
	for cartridge in 1 2 3 4 5 6 7 8
	do
		for server in 1 2
		do
			id="$chassis$cartridge$server"
			host_ip="20.200.10.$id"
			source_dir="$source_root_dir/$host_ip"
			cmd="scp $source_dir/ifcfg-* root@$host_ip:/etc/sysconfig/network-scripts/"
            echo $cmd
            $cmd
			cmd="scp $source_dir/interfaces root@$host_ip:/etc/network/interfaces"
			echo $cmd
			$cmd
		done
	done
done

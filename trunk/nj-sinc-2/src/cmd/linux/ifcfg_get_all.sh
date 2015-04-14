#!/bin/sh

target_root_dir="/tmp/ifcfg"
echo "cleaning $target_root_dir ..."
cmd_rm="rm -fr $target_root_dir/*"
echo $cmd_rm
$cmd_rm


for chassis in 1
do
	for cartridge in 1 2 3 4 5 6 7 8
	do
		for server in 1 2
		do
			id="$chassis$cartridge$server"
			host_ip="20.200.10.$id"
			target_dir="$target_root_dir/$host_ip"
			mkdir -p $target_dir
			cmd="scp root@$host_ip:/etc/sysconfig/network-scripts/ifcfg* $target_dir"
            echo $cmd
            $cmd
			cmd="scp root@$host_ip:/etc/network/interfaces $target_dir"
			echo $cmd
			$cmd
		done
	done
done

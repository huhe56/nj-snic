#!/bin/sh

target_root_dir="/tmp/medusa_bad"
echo "cleaning $target_root_dir ..."
cmd_rm="rm -fr $target_root_dir/*"
echo $cmd_rm
$cmd_rm


for chassis in 1
do
	for cartridge in 2 3
	do
		for server in 1 2
		do
			id="$chassis$cartridge$server"
			host_ip="20.200.10.$id"
			target_dir="$target_root_dir/$host_ip"
			mkdir -p $target_dir
			cmd="scp -r root@$host_ip:/mnt/$id/* $target_dir"
			echo $cmd
			$cmd
		done
	done
done
tar cvfz /tmp/medusa_bad.tar.gz /tmp/medusa_bad
			

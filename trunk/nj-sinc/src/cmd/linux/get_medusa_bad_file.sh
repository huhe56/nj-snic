#!/bin/sh

target_root_dir="/tmp/medusa_bad"
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
			target_dir="$target_root_dir/$host_ip/1"
			mkdir -p $target_dir
			cmd="scp root@$host_ip:/root/tools/medusa/shell/*/*.bad $target_dir"
			echo $cmd
			$cmd
			if [ $server = "2" ]; then
				target_dir2="$target_root_dir/$host_ip/2"
				mkdir -p $target_dir2
				cmd2="scp root@$host_ip:/root/tools/medusa/shell-sdb/*/*.bad $target_dir2"
				echo $cmd2
				$cmd2
			fi
		done
	done
done
tar cvfz /tmp/medusa_bad.tar.gz /tmp/medusa_bad
			
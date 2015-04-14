#!/bin/sh

clean=false

target_root_dir="/tmp/var_log_msg"

if [ "$clean" = true ]; then
	echo "cleaning $target_root_dir ..."
	cmd_rm="rm -fr $target_root_dir/*"
	echo $cmd_rm
	$cmd_rm
fi

for chassis in 1
do
	for cartridge in 2
	do
		for server in 1
		do
			id="$chassis$cartridge$server"
			host_ip="20.200.10.$id"
			target_dir="$target_root_dir/$host_ip"
			mkdir $target_dir
			cmd="scp root@$host_ip:/var/log/messages* $target_dir"
			echo $cmd
			$cmd
		done
	done
done

echo "generating tar.gz file ..."
tar cvfz /tmp/var_log_msg.tar.gz /tmp/var_log_msg
			
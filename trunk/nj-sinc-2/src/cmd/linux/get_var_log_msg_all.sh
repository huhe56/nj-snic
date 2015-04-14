#!/bin/sh

target_root_dir="/tmp/var_log_msg"
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
            if [ "$cartridge" -eq 7 ] || [ "$cartridge" -eq 8 ]; then  
			    cmd="scp root@$host_ip:/var/log/syslog* $target_dir"
            else
			    cmd="scp root@$host_ip:/var/log/message* $target_dir"
            fi
			echo $cmd
			$cmd
		done
	done
done
tar cvfz /tmp/var_log_msg.tar.gz /tmp/var_log_msg
			

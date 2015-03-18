#!/bin/sh

./run_shell_cmd.py echo " "\; echo "------ boot LUN"\; ps -ef \| grep shell \| grep host \| grep -v grep\; echo ""\; sleep 2\; tail /root/tools/medusa/shell/host*.log\; echo "------ data LUN "\; ps -ef \| grep data \| grep host \| grep -v grep\; echo ""\; sleep 2\; tail /data/host-*.log

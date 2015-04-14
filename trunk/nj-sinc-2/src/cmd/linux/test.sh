#!/bin/bash


cmd="gnome-terminal -x sh -c 'ls; date; echo.sh; exec bash; echo.sh'"
echo $cmd
$cmd


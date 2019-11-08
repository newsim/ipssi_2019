#!/bin/bash

set -e

if [ -z 'www.google.com' ];then
	echo "donnez un nom de site"
	exit 1
else
	if curl -s -I 'www.google.com' >/dev/null ;then
		echo $(date '+%Y-%m-%d %H:%M:%S') "internet OK" >> internet.log
	else
        echo $(date '+%Y-%m-%d %H:%M:%S') "internet FAIL" >> internet.log
		exit 2
	fi
fi


exit 0

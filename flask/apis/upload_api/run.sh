#! /bin/bash

if [ -d 'uploaded/' ]
then
	echo 'directory exist'
else
	mkdir uploaded
fi

python3 upload.py

#! /bin/bash

if [ -d 'images' ]
then
	echo 'directory exist'
else
	mkdir images
fi

python3 app.py

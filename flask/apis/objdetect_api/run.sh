#! /bin/bash

if [ -d 'images' ]
then
	echo 'directory exist'
else
	mkdir images
fi

if [ -e 'yolo-coco/yolov3.weights' ]
then
		echo 'service ready'
else
		echo '!! Cannot find file: yolo-coco/yolov3.weights !!'
		echo 'Service ABORTED'
		exit 1
fi

python3 app.py

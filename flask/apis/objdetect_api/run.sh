#! /bin/bash

if [ -d 'images' ]
then
	echo 'directory exist'
else
	mkdir images
fi

if [ -d 'stitch' ]
then
	echo 'directory exist'
else
	mkdir stitch
fi

if [ -e 'yolo-coco/yolov3.weights' ]
then
		echo 'service ready'
else
		echo '!! Cannot find file: yolo-coco/yolov3.weights !!'
        echo 'downloading yolov3.weights......'
        cd yolo-coco
        wget https://pjreddie.com/media/files/yolov3.weights
        cd ..
fi

python3 app.py

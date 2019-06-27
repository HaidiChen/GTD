# NOTICE:
yolov3.weights file is missing in this api as it is too big.
But you can download one from the yolo-coco folder.

# ISSUE:
if facing an error caused by:
ImportError: libSM.so.6: cannot open shared object file.

run following commands:
$ sudo apt install -y libsm6 libxext6
$ sudo apt install -y libxrender-dev

# USAGE
1. first start the service:
   !! PLEASE remember to DOWNLOAD the yolov3.weights file and put it 
      in the yolo-coco folder before starting the service !!

$ bash run.sh

2. use the following command to upload an image and see the result.
   Assume that the image is JPG file

$ curl -F "file=@<img_path>" http://Service_IP_Address:5000/detect -X POST --output result.<img_ext>

# DISCOVERY
this object detection algorithm seems having trouble detecting puppies.
I tried to detect the puppy using the image below but it detected nothing.

https://i.ytimg.com/vi/p079QtWvf7o/maxresdefault.jpg

However, it detected the puppy in the following image even though these two
images are essentially showing the same puppy.

https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_T8wayt7zzA-k4Bssoqn4OvHowoTdQh4cFXiveClDdQ9__faT

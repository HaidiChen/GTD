# NOTICE:
yolo3.weights file is missing in this api as it is too big.
But you can download one from the yolo-coco folder.

# ISSUE:
if facing an error caused by:
ImportError: libSM.so.6: cannot open shared object file.

run following commands:
$ sudo apt install -y libsm6 libxext6
$ sudo apt install -y libxrender-dev

# USAGE
use the following command to upload an image and see the result.
Assume that the image is JPG file

$ curl -F "file=@<image_path>" http://IP_Address:5000/detect -X POST --output result.jpg

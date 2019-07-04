from imutils import paths
import argparse
import imutils
import cv2

def stitch(images_path, output_path):
    print("[INFO] loading images...")
    imagePaths = sorted(list(paths.list_images(images_path)))
    images = []

    # loop over the image paths, load each one, and add them to our
    # images to stitch list
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)

    # initialize OpenCV's image stitcher object and then perform the image
    # stitching
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite(output_path, stitched)
        return True

    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))
        return False

#there are many more color spaces than RGB
#e.g. the HSV color space is more similar to how humans conceive of color
#OpenCV provides support for many of these color spaces

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#converts the image from the RGB color space to grayscale by specifying the cv2.COLOR_BGR2GRAY flag
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #converts image to HSV color space by specifying the cv2.COLOR_BGRHSV flag
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) #convert to the L*a*b* color space by using the cv2.COLOR_BGR2LAB flag
cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)

#thresholding = binarization of an image, converting grayscale to a binary image
#simple thresholding requires specifying a threshold value T --> pixels below T set to 0 and pixels greater than T are set to 255

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting image from RGB color space to grayscale
blurred = cv2.GaussianBlur(image, (5, 5), 0) #apply Guassian blyrring with radius of 5, helps remove some high frequency edges we aren't concerned with
cv2.imshow("Image", image)
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY) #computing the threshold image, first argument is the grayscale image we want to threshold, setting T value to 255
cv2.imshow("Threshold Binary", thresh) #applying inverse thresholding
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2. THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv)) #perform masking --> part of the image will be revealed and the rest will be hidden
cv2.waitKey(0)

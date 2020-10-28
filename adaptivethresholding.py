import numpy as np
import argparse
import cv2
#adaptive thresholdhing = don't have to manually supply T value
ap = argparse.ArgumentParser() #constructing arg parser and loading image
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting image to grayscale and blurring it slightly
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4) #applying adaptive thresholding using cv2.adaptiveThreshold function, first parameter is image we want to threshold, then max value, then compute the threshold for the current neighborhood of pixels
cv2.imshow("Mean Thresh", thresh)
thresh = cv2.adaptiveThreshold(blurred, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)

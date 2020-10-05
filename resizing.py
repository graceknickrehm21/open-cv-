import cv2
import numpy as np

import numpy as np
import argparse
import imutils
import cv2

#resizing images
ap = argparse.ArgumentParser()#lines 10-16 set up the argument parser and loading and displaying the image
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0 / image.shape[1] #computing the aspect ratio --> proportional relationship of the width and the height of the image. This line defines the width of the image to be 150 pixels, image shape accesses the old width
dim = (150, int(image.shape[0] * r)) #compute the new dimensions of the image --> multiply the old height by the aspect ratio and convert it to an integer

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) #actual resizing takes place, first argument is the image being resized, second is the dimensions for the new image, and the last is the interpolation method (alogrithm that handles how the actual image is resized)
cv2.imshow("Resized (Width)", resized) #showing the resized image
#Note: can also resize the image by specifying the height

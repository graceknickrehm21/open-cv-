import cv2
import numpy as np

import numpy as np
import argparse
import imutils
import cv2

#image rotations --> rotating an image by some angle x
ap = argparse.ArgumentParser() #construcing an argument parser with the path to the image
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])#loading and displaying the image
cv2.imshow("Original", image)

(h, w) = image.shape[:2] #defining height and width of the image
center = (w // 2, h // 2) #defining the center of the image

M = cv2.getRotationMatrix2D(center, 45, 1.0)#defining a matrix to rotate the image
#cv2.getRotationMatrix2D function takes three arguments: the point to rotate the image around, the number of degrees we are going to rotate the image by, and the scale of the image (1.0 = same dimensions of the image are used)
rotated = cv2.warpAffine(image, M, (w, h)) #apply the rotation to the image using the cv2.warpAffine method
cv2.imshow("Rotated by 45 Degrees", rotated)#shows image rotated by 45 degrees

M = cv2.getRotationMatrix2D(center, -90, 1.0)#perform another rotation, this time by -90 degrees instead of 45

rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

#much more efficient way to do rotations than making calls to cv2.getRotationMatrix2D and cv2.warpAffine each time you want to rotate an image
rotated = imutils.rotate(image, 180) #rotates image 180 degrees
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

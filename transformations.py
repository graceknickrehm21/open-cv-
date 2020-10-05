import cv2
import numpy as np

#translation --> shifting an image along the x and y axis (up, down, left, or right)
import numpy as np #importing the packages we will use
import argparse
import imutils #new package, library you write yourself to create conveinice methods to do rotations, translations, and resizings
import cv2

ap = argparse.ArgumentParser() #constructing the argument parser and loading our images
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]]) #define translation matrix M as a floating point array
#[1,0,x] is the first row of the array where x is the # of pixels I shift the image left or right --> negative x shifts the image left and positive x shifts the image right
#second row of the matrix is [0,1,y] where y is the # of pixels we shift the image up or down --> negative y shifts the image up and positive y shifts the image down
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))#iniaties actual translation, first argument is the image being shifted and the second argument is the translation matrix M, third argument is the dimensions (width and height) of the image (manually supplied)
cv2.imshow("Shifted Down and Right", shifted)#shows the result of the translation

M = np.float32([[1, 0, -50], [0, 1, -90]])#shifting 50 pixels left and 90 pixels up (left and up, not right and down, because I use negative values)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100) #shifts the image down 100 pixels
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

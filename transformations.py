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

#actual translation takes places on lines 23-25
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


#resizing images
ap = argparse.ArgumentParser()#lines 63 through 69 set up the argument parser and loading and displaying the image
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

#flipping --> can flip an image around on the x or y axis, or both

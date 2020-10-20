import numpy as np
import argparse
import cv2

#questions
#for the blurring, how can I make sure it's blurring just the background?

#goals
#take an image of Bishop’s students walking across the quad
#heavily blur the part where the students aren’t (gimp blurs images)
#count how many people are on the quad
#detect who is a senior based on the color of their shirt
#detect what time of day it is
#if it’s before noon, make them invisible (look at metadata of a photo, look at time stamp)


ap = argparse.ArgumentParser() #lines 14-33 set up the argument parser and load and save the images
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

img1 = cv2.imread('quadimage1.png',0)
cv2.imshow('image 1',img1)
cv2.imwrite('image 1',img1)

img2 = cv2.imread('quadimage2.png',0)
cv2.imshow('image 2',img2)
cv2.imwrite('image 2',img2)

img3 = cv2.imread('quadimage3.png',0)
cv2.imshow('image 3',img3)
cv2.imwrite('image 3',img3)

img4 = cv2.imread('quadimage4.png',0)
cv2.imshow('image 4',img4)
cv2.imwrite('image 4',img4)

#bilateral blurring is able to preserve edges of an image, while still reducing noise, but is considerably slower than its averaging, Gaussian, and median blurring counterparts.
blurred = np.hstack([
cv2.bilateralFilter(img1, 5, 21, 21))] #First parameter is the image being blurrend, then we define the diameter of our pixel neighborhood. The third argument is our color σ (larger σ means  more colors in the neighborhood will be considered when computing the blur) fourth arg is the space σ (larger value of space σ means that pixels farther out from the central pixel will influence the blurring calculation)
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.bilateralFilter(img2, 5, 21, 21))]
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.bilateralFilter(img3, 5, 21, 21))]
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.bilateralFilter(img4, 5, 21, 21))]
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

#convert the colored image into binary image and then use bitwise OR so that the background is white and the people are colored
(thresh, img1) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('bw_image.png', img1)

#need to find a color that is in all the people but not in everything else 
#pixel is turned off if it has a value of zero and on if it has a value greater than zero
#OR: A bitwise OR is true if either of the two pixels are greater than zero.
bitwiseOr = cv2.bitwise_or(img1) #applying OR to the shapes
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

import cv2 #lines 1-13 follow standrd procedure of importing packages, parsing arguments, and loading the image
import argparse
import imutils


#flipping --> can flip an image around on the x or y axis, or both
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1) #flips the image, requires two arguments: the image being flipped and a flip code value that determines is used to determine how the image is flipped
#flip code value of one means the image will be fipped horizontally, a flip code value of 0 means we will flip vertically, and a negative flip code flips the image around both axes
cv2.imshow("Flipped Horizontally", flipped)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

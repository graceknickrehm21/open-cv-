#using a mask lets you look at the code in portions
import numpy as np #import packages
import argparse
import cv2

ap = argparse.ArgumentParser() #parse arguments
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) #load images
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype = "uint8") #comstruct a NumPy array filled with zeros with the same width and height as the image that will be masked
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)#computing the center of the image
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)#drawing the white rectangle
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)#apply a mask using cv2.bitwise_and function --> first two parameters are the image itself, supply the mask function makes sure the bitwsie function only examines pixels that are on the mask (in this case, part of the white rectangle)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

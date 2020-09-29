#exploring how to split an image into its respective components

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image) #splits the channels
#Remember, OpenCV stores RGB images as NumPy arrays in reverse channel order
cv2.imshow("Red", R)#showing each channel individually
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R]) #merging the channels back together using cv2.merge
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
zeros = np.zeros(image.shape[:2], dtype = "uint8")#construct a NumPy array of zeroes with the same width and height as our original iamge
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))#constructs a red channel represntation of the image but sepcifices zeros array for green and blue channels
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

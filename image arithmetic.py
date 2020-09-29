#image arithmetic
#remember there is a difference between OpenCV and NumPy addition --> NumPy performs a wrap around method and OpenCV performs clipping to ensure pixel values never fall outside the range [0,255]
#clipping method: setting max and min values for pixels
#wrap around method: the amount above 250 or below 0 that the inputed number goes will be added or subtracted, e.g. 0-10 would become 246, and 250 + 10 would become 4

from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8 #defines two NumPy arays that are 8-bit unsigned integers --> first arrawy has one element (a value of 200), and the second has one element (a value of 100),then they are added together using cv2.add --> should return a value of 255
([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8#performs subtraction using cv2.subtract --> openCV performs clipping, so the value is clipped to 0
([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

#using NumPy to perform the arithmetic instead of OpenCV --> uses wrap around method
max of 255: [[255]] #defining two NumPy arrays
min of 0: [[0]]

#performing the arithmetic on images
M = np.ones(image.shape, dtype = "uint8") * 100 #defines a NumPy array of ones with the same size as the image
#use the cv2.add funtion to add the matrix of 100s to the original image --> increasing each pixel intensity in the image by 100 but making sure they are clipped to the range [0,255]
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50 #create a NumPy array filled with 50s
subtracted = cv2.subtract(image, M) #use cv2.subtract function to subtract 50 from each pixel intensity -->  makes the image darker
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

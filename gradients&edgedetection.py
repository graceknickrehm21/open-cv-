#edge detection = using math to find points in an image where the brightness of pixel intensities changes distincly
import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
lap = cv2.Laplacian(image, cv2.CV_64F) #using laplacian method to compute the gradient magnitude image, first arg is grayscale image, second arg is data type for the outut image, using 64 bit flow
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)#first arg=image we are computing the gradient representation for, last two args are the order of the derivatives in the x and y direction
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))#ensure we find all edges by taking abs val of the floating point integer and converting it to an 8-bit unsigned integer
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)#combine gradient images in both x and y direction by applying a bitwise OR --> OR is true when either pixel is greater than zero, so it is true if either a horizontal or vertical edge is present

cv2.imshow("Sobel X", sobelX)#show gradient images
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

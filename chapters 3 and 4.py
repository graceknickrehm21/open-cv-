import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
#importing the packages I need and setting up an argument parser

(b, g, r) = image[0, 0] #grab the pixel located at (0,0)
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b)) #prints out the values of each channel to our console.

image[0, 0] = (0, 0, 255)#manipulate the top left pixel value to have a value of (0,0,255) --> red color, OpenCV stores RGB pixels in reverse order --> BGR
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b) #grab the pixel value and print it back to console to prove that color of the pixel was successfully changed
corner = image[0:100, 0:100] #grab a 100 × 100 pixel region of the image, must provide start and end y and x
cv2.imshow("Corner", corner) #shows the result of the cropping

image[0:100, 0:100] = (0, 255, 0)#accessing the top-left corner of the image --> setting  region to have a value of (0, 255, 0), green

cv2.imshow("Updated", image)
cv2.waitKey(0)

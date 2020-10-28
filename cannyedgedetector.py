import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0) #by blurring the image we remove "noisy" edges that aren't of interest
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30, 150)#canny detector applied, first arg = blurred, grayscale image, then two threshold values, any value below threshold1 is not an edge
cv2.imshow("Canny", canny) #showing results of the edge detection
cv2.waitKey(0)

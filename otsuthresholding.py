from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2
#otsu thresholding is another way we can automatically compute the threshold value T --> assumes there are two peaks in the grayscale histogram of the image and tries to find an optimal value to seaparate those peaks
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert image to grayscale and blur slightly
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)
T = mahotas.thresholding.otsu(blurred)
print("Otsu’s threshold: {}".format(T))
thresh = image.copy()#threshold applied lines 18-21 --> line 18 we make a copy of grayscale image so we have image to threshold
thresh[thresh > T] = 255 #any values greater than T are white
thresh[thresh < 255] = 0 #remaining pixels are made black 
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)

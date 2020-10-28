#contour = curve of points with no gaps in the curve --> useful for shape approximation and analysis
#need to obtain a binariztion of an image before applying contour

from __future__ import print_function #set up the environment by importing packages, parsing arguments, and loading the image
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150) #obtain edged image by applying cannny edge detector, any gradient values below thirty are non-edges and any values above 150 are sure edges
cv2.imshow("Edges", edged)
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #finding the contours of the outlines --> returns a tuple of our image after contour detection is applied, the contours themselves, and the hierarchy of contours, this function is destructive to the image you pass in
print("I count {} coins in this image".format(len(cnts)))
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
#cropping each individual coin from the image
for (i, c) in enumerate(cnts):
(x, y, w, h) = cv2.boundingRect(c)
print("Coin #{}".format(i + 1))
coin = image[y:y + h, x:x + w]
cv2.imshow("Coin", coin)
mask = np.zeros(image.shape[:2], dtype = "uint8")
((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
cv2.circle(mask, (int(centerX), int(centerY)), int(radius),255, -1)
36 mask = mask[y:y + h, x:x + w]
37 cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask =
mask))
38 cv2.waitKey(0)

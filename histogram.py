
#histogram = distribution of pixel intensities in an image
#represented as a graph, bins on the x axis, number of pixels binned on the y axis

from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser() #Importing the packages we need, setting up an argument parser, and loading the image
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#converting image from RGB color space to gray scale
cv2.imshow("Original", image)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])#computes histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist) #plots histogram
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

#if very few pixels fall in the range 200 to 255, that means there are very few "white" pixels in the image

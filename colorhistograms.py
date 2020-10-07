from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

chans = cv2.split(image) #splitting the image into its three channels (blue, green, and red, because OpenCV sores the image as a NumPy in reverse order)
colors = ("b", "g", "r") #initializing a tuple of strings representing each of the colors
plt.figure#setting up the PyPlot figure
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
hist = cv2.calcHist([chan], [0], None, [256], [0, 256])#computing a histogram for each red, green, and blue channel
plt.plot(hist, color = color)
plt.xlim([0, 256])
#most applications use between 8 and 64 pixels when computing multi-dimensional histograms
#2D histogram is sored as a 2D NUmpy array 

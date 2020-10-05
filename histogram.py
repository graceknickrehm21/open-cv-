
#histogram = distribution of pixel intensities in an image
#represented as a graph, bins on the x axis, number of pixels binned on the y axis

from matplotlib import pyplot as plt
2 import argparse
3 import cv2
4
5 ap = argparse.ArgumentParser()
6 ap.add_argument("-i", "--image", required = True,
7 help = "Path to the image")
8 args = vars(ap.parse_args())
9
10 image = cv2.imread(args["image"])

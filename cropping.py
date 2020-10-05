#cropping an image --> removing outer parts we are not interested in, done using NUmPy array slicing
#cropping is essentially performing array slices on NumPy arrays 

import numpy as np #lines 3-14 handle importing packages, parsing arguments, and loading images
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[30:120 , 240:335] #actual cropping taking place --> NumPy array slices specify which rectangular region of the image will be extracted, OpenCV represents images as NumPy arrays with height first and width second --> y-axis values go before x-axis values
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)

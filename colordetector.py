#import the necessary packages
from imutils.object_detection
import non_max_suppression
import numpy as np
import imutils #lets you perorm transfomations from the results
import cv2 #OpenCV Python wrapper
import requests #lets yousend data/results
import time
import argparse #lets you read commands from the command terminal inside the script

# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image") #--image is path to where the image resides on disk
args = vars(ap.parse_args())
#load the image off disk
image = cv2.imread(args["image"])

#want to be able to detect maroon color
#define the list of boundaries
boundaries = [
	([100,0,0], [175,0,0]) #maroon is (128,0,0)
]
#use cv2.inRnage function to perform the actual color detection
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8") #converting the upper and lower limits to NumPy arrays
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper) #expects three arguments: the image, the lower limit of the color you want to detect, and the upper limit of the color you want to detect
	output = cv2.bitwise_and(image, image, mask = mask) #binary mask is returned where white pixels (255) represent pixels that fall into the upper and lower liit range, and black pixles (0) do not
	# show the images, will only show the pixels in the image that have a corresponding white (255) value in the mask
	cv2.imshow("images", np.hstack([image, output])) #displays output images
	cv2.waitKey(0)

#Basic steps
#To detect colors in images,  define the upper and lower limits for your pixel values.
#Once those are defined, make a call to the cv2.inRange method, which returns a mask specifying which pixels fall into the specified upper and lower range.
#once you have the mask, you can apply it to your image using the cv2.bitwise_and function.

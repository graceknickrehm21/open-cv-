import cv2
import numpy as np #this code explores chapter 5 concepts --> using cv2 to draw shapes on images

canvas = np.zeros((300, 300, 3), dtype = "uint8") #defining an image manually by constructing a numpy array with 300 rows and columns and allocate space for three channels
#np.zeroes fills every element in the array with an initail value of zero
#dtype sets the datatype to an 8-bit unsigned integer

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green) #draw a green line from point (0, 0) (the top-left corner of the image) to point (300, 300), the bottom-right corner of the image
cv2.imshow("Canvas", canvas #show the image and then wait for a key press
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3) #draw a red line from the top-right corner of the image to the bottom left, last parameter to the method controls the thickness of the line – setting it to 3 pixels
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

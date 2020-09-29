#bitwise operations: AND, OR, XOR, and NOT
#represented as grayscale images
#pixel is turned off if it has a value of zero and on if it has a value greater than zero

#binary operations
#AND: A bitwise AND is true if and only if both pixels are greater than zero.
#OR: A bitwise OR is true if either of the two pixels are greater than zero.
#XOR: A bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both.
#NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.

import numpy as np #importing the packages needed
import cv2

rectangle = np.zeros((300, 300), dtype = "uint8") #initializes rectangle image as a 300 by 300 numpy array
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1) #drawing a 250 x 250 white rectangle at the image center
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8") #initalize an image to contain a circle
cv2.circle(circle, (150, 150), 150, 255, -1) #circle is centered at the center of the image with a radius of 150 pixels
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)#applying AND to the rectangle and circle images --> rectangle doesn't cover as large an area as the circle so both pixels should be off
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle) #applying OR to the shapes
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle) #applying XOR function to the shapes --> center of square is removed because XOR operation cannot have both pixels greater than zero
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle) #applying the NOT function to flip pixel values --> pixels greater than zero are set to zero and pixels set to zero are set to 255
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

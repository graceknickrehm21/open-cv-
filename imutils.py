import numpy as np #creating a new file that will store image processing methods so they can be easily called without a lot of code
import cv2

def translate(image, x, y): #defining a translate function, takes in three parameters: image being translated, # of pixels shifting along the x-axis, and the # of pixels the image will be shifted along the y axis
M = np.float32([[1, 0, x], [0, 1, y]]) #defining translation matrix M
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) #actual shift

return shifted #returns the shifted image

def rotate(image, angle, center = None, scale = 1.0):#defining own custom rotate method
#rotate method takes four arguments:the image, the angle we want to rotate the image, the point we want to rotate the image around, and the scale to handle whether the size should be changed
(h, w) = image.shape[:2]

if center is None:
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, angle, scale)#constructing the rotation matrix
rotated = cv2.warpAffine(image, M, (w, h))#appy it to the image

return rotated #return the rotated image

#defining a resized method
resized = imutils.resize(image, width = 100) #actual resizing is handled by a single function, first argument is the image being resied, second is the keyboard argument width, which is the width of the new image

cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

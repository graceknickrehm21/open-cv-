import numpy as np
import cv2
#Experimenting with the basic operations on images

# Load an color image in grayscale
img = cv2.imread('bishops.jpeg',0)

#display an image in a window
cv2.imshow('image',img)
cv2.waitKey(0) #keyboard binding function
cv2.destroyAllWindows() #can use cv2.destroyWinow()to destroy a specific destroyAllWindows

#save an image
cv2.imwrite('bishops.png',img)

#access a pixel value using row and column coordinates
px = img[100,100]
print px

# accessing only blue pixel
blue = img[100,100,0]
print blue
#Note: for individual pixel access, Numpy array methods, array.item() and array.itemset() are better

#Shape of image is accessed by img.shape --> returns a tuple of number of rows, columns and channels
print img.shape

#Total number of pixels is accessed by img.size
print img.size

#Image datatype is obtained by img.dtype
print img.dtype
#important for debugging because lots of errors in OpenCV Python code are caused by invalid data types

#Region of interests are obtained using Numpy indexing
tower = img[280:340, 330:390] #not actually the correct coordinates
img[273:333, 100:160] = tower

#splitting B,G, R channels of an image into their individual planes
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
#Note: cv2.split() is a costly operation (in terms of time), so only use it if necessary --> Numpy indexing is much more efficient

#create a border around the image
cv2.copyMakeBorder()

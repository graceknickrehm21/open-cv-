import cv2
import numpy as np #this code explores chapter 5 concepts --> using cv2 to draw shapes on images

canvas = np.zeros((300, 300, 3), dtype = "uint8") #defining an image manually by constructing a numpy array with 300 rows and columns and allocate space for three channels
#np.zeroes fills every element in the array with an initail value of zero
#dtype sets the datatype to an 8-bit unsigned integer

#LINES
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green) #draw a green line from point (0, 0) (the top-left corner of the image) to point (300, 300), the bottom-right corner of the image
cv2.imshow("Canvas", canvas #show the image and then wait for a key press
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3) #draw a red line from the top-right corner of the image to the bottom left, last parameter to the method controls the thickness of the line – setting it to 3 pixels
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#RECTANGLES
cv2.rectangle(canvas, (10, 10), (60, 60), green)#first argument is the image you draw your rectangle on, second is the starting position of the rectangle, third is the ending point, last argument is the color of the rectangle
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)#final argument determines the thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)#specifiying a negative value for thickness makes it a solid blue line
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#CIRCLES
canvas = np.zeros((300, 300, 3), dtype = "uint8") #makes the canvas blank
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2) #defines the X and Y coordinates of the center of the image
white = (255, 255, 255) #defines a white pixel
#image is found using canvas.shape[0] and the width using canvas.shape[1]

for r in range(0, 175, 25): #loop over different radius values incrementing by 25 each step
cv2.circle(canvas, (centerX, centerY), r, white) #first parameter sets the canvas, and then I pass a tuple that provides the point in which the circle will be drawn around

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


#ABSTRACT DRAWING
for i in range(0, 25): #generating random circles using three values: the radius, color, and coordinates
radius = np.random.randint(5, high = 200)#generating a radius in the range [5,200)
color = np.random.randint(0, high = 256, size = (3,)).tolist #randomly generating a color of an RGB pixel -- has three values in the range [0,255], passing the argument size=3 instructs NumPy to return a list of 3 numbers
()
pt = np.random.randint(0, high = 300, size = (2,)) #generating a random point to draw the circle using np.random.randint function

cv2.circle(canvas, tuple(pt), radius, color, -1)#make a circile using the radius, color, and point that was generated, use a thickness of -1 so the circles are a solid color and not an outline

cv2.imshow("Canvas", canvas) #display the circle
cv2.waitKey(0)

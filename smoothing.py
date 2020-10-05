#blurring = each pixel in the image is mixed in with surrounding pixel intensities
import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])#loading image and showing it as a baseline to compareb blurring methods to
cv2.imshow("Original", image)

#averaging --> uses simple mean
blurred = np.hstack([ #stack images together rather than create three separate windows
cv2.blur(image, (3, 3)), #two arguments are the image you want to blur and the size of the kernel
cv2.blur(image, (5, 5)),
cv2.blur(image, (7, 7))]) #increasing sized-kernels --> image is more blurred
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

#gaussian blurring --> uses weighted mean, pixels closer to the central pixel contribute more weight to the average
blurred = np.hstack([
cv2.GaussianBlur(image, (3, 3), 0), #image we want to blur, kernel size, and standard deviation in the x-axis direction, setting it to zero instructs OpenCV to automatically compute them based on kernel size
cv2.GaussianBlur(image, (5, 5), 0),
cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

#median method --> replace central pixel with the median pixel, so each central pixel is always replaced with a pixel intensity that exists in the image
blurred = np.hstack([
cv2.medianBlur(image, 3), #parameters: image we want to blur and the size of the kernel
cv2.medianBlur(image, 5),
cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

#bilateral --> allows you to reduce noise while still maintaining edges, slower than the other methods
blurred = np.hstack([
cv2.bilateralFilter(image, 5, 21, 21), #third argument is the color, larger color value means more colors will be considered when computing the blur, fourth argument is the space (larger value means that pixels farther out from the central pixel will influence the blurring calculation)
cv2.bilateralFilter(image, 7, 31, 31),
cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

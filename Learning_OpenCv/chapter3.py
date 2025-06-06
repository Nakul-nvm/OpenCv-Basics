import cv2
import numpy as np

# RESIZING AND CROPPING

img = cv2.imread("Resources/lambo.png")

print(img.shape)# output = ( height, width , no of channels {eg = 3 -> BGR})

imgResize = cv2.resize(img , (300,200))

print(imgResize.shape)

imgCropped = img[0:200,200:400] # using a matrix function not a cv2 function (first range is for height, second range is for width)

cv2.imshow("Output",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)
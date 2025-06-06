import cv2
import numpy as np

# BASIC FUNCTIONS

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray , (7,7),0) # kernel size can be of odd number (5,5),(7,7) etc..
imgCanny = cv2.Canny(img , 150, 200)
imgDialation = cv2.dilate(imgCanny ,kernel , iterations=1)
imgEroded = cv2.erode(imgDialation , kernel , iterations=1)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



cv2.imshow("gray image", imgGray)
cv2.imshow("blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
# cv2.imshow("dialation image", imgDialation)
# cv2.imshow("eroded image", imgEroded)
cv2.imshow("HSV", imgHSV )

cv2.waitKey(0)
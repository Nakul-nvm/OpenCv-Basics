import cv2
import numpy as np

#SHAPES AND TEXTS 

img = np.zeros((512,512,3), np.uint8) # this image has 3 channels BGR
# print (img.shape)
# img[:] = 255, 0, 0 # img[:] here colon represents whole image and we put colon between value we can range  the color on image

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(0,0),(200,300),(255,0,0),5)
cv2.rectangle(img,(200,0),(400,300),(255,255,0),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,0,255),5)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)



cv2.imshow("output", img)
cv2.waitKey(0)
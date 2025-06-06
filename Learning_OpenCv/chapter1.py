import cv2
print ("package imported")

# # reading the image file

# img = cv2.imread("Resources/lena.png")

# cv2.imshow("output", img)

# cv2.waitKey(0) # 0 -> wait for infinite delay & any other number means that many milliseconds





# # read the video file

# cap = cv2.VideoCapture("Resources/test.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("output", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): # adds a one sec delay and runs video till 'q' key is pressed
#         break




#  opening the webcam

cap = cv2.VideoCapture(0)
cap.set(3,640) # id 3 = width
cap.set(4,480) # id 4 = height
cap.set(10,100) # id 10 = brightness


while True:
    success, img = cap.read()
    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # adds a one sec delay and runs video till 'q' key is pressed
        break
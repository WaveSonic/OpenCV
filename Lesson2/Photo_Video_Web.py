import cv2

#Photo
#img = cv2.imread('../images/image.jpg')
#cv2.imshow('Result', img)
#cv2.waitKey(0)


#Video
#cap = cv2.VideoCapture('../videos/video.mp4')

#while True:
    #succes, img = cap.read()
    #cv2.imshow('Result', img)

    #if cv2.waitKey(10) & 0xFF == ord('q'):
        #break


#Web-Camera
cap = cv2.VideoCapture(0)
"""Setting"""
cap.set(3, 500)
cap.set(4, 500)

while True:
    succes, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.Canny(img, 100, 140)
    cv2.imshow('Result', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break





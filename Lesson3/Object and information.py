import cv2
import numpy as np

photo = np.ones((300, 300, 3), dtype='uint8')
#photo[10:150, 200:280] = 0, 0, 255 #Format BlueGreenRed

cv2.rectangle(photo, (50, 0), (60, 100), (119, 201, 105), thickness=cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (100, 0, 0), thickness=3) #Lines

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=1) #Circle

cv2.putText(photo, 'Hello', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1) #Text
cv2.imshow('Photo', photo)
cv2.waitKey(0)
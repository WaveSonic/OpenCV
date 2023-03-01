import cv2
import numpy as np

img = cv2.imread('../images/image.jpg') #load image
new_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) #resize
img = cv2.GaussianBlur(img, (9, 9), 0) #Blur
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Image to grey
img = cv2.Canny(img, 70, 70) #Image to binary (May after convert to gray)

kernel = np.ones((5, 5), np.uint8) #create kernel
img = cv2.dilate(img, kernel, iterations=1) #Увеличение обводки
img = cv2.erode(img, kernel, iterations=1) #Уменьшаем обводку
cv2.imshow('Result', img) #Show image
cv2.waitKey(0) #Time show image (if 0 - infinity)


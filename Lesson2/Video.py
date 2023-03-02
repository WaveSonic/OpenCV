import cv2
import numpy as np
cap = cv2.VideoCapture('../videos/video.mp4')

while True:
    succes, img = cap.read()
    img = cv2.GaussianBlur(img, (9, 9), 0)  # Blur
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Image to grey
    img = cv2.Canny(img, 100, 100)  # Image to binary (May after convert to gray)

    kernel = np.ones((5, 5), np.uint8)  # create kernel
    img = cv2.dilate(img, kernel, iterations=1)  # Увеличение обводки
    img = cv2.erode(img, kernel, iterations=1)  # Уменьшаем обводку
    cv2.imshow('Result', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
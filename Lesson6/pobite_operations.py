import cv2
import numpy

photo = cv2.imread('../images/image.jpg')
img = numpy.zeros((photo.shape[:2]), dtype='uint8')

#img = numpy.zeros((350, 350), dtype='uint8')
circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)
#img = cv2.bitwise_or(circle, square)
#img = cv2.bitwise_xor(circle, square)
#img = cv2.bitwise_not(square)

cv2.imshow('Hello', img)
cv2.waitKey(0)
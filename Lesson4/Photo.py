import cv2
import numpy as np
img = cv2.imread("../images/image.jpg")

#img = cv2.flip(img, -1) #Flip image

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width//2, height//2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (width, height))

def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    print(img_param.shape)
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param[0]))

#img = transform(img, 30, 200)
#img = rotate(img, 270)
cv2.imshow('Result',img)
cv2.waitKey(0)
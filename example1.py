import cv2
import numpy as np

img=cv2.imread('b.jpg')
px=img[100, 100]
print px
blue = img[100, 100, 0]
print blue
ball = img[200:800, 200:800]
img[10:610, 10:610] = ball

cv2.imshow('a', img)
cv2.waitKey(0)


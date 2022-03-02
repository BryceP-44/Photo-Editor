import cv2
import numpy as np
import random

img=cv2.imread('blur.png')

h,w,channels=img.shape

for i in range(h):
    for j in range(w):
        if (i/h)>random.random():
            img[i][j]=0,0,0


cv2.imshow('image',img)            
cv2.imwrite('newblock.png',img) 

import cv2
import numpy as np

img=cv2.imread('block2.png')

h,w,channels=img.shape
imgn=cv2.imread('block2.png')


thresh=10

for i in range(1,h-1):
    if i%10==0:
        print(round(i/h*100),"%")
    for j in range(1,w-1):
        b,g,r=img[i][j]
        if b<thresh or g<thresh:
            imgn[i+1][j+1]=0,0,0
            imgn[i+1][j]=0,0,0
            imgn[i-1][j]=0,0,0
            imgn[i][j+1]=0,0,0
            imgn[i][j-1]=0,0,0
            imgn[i-1][j+1]=0,0,0
            imgn[i-1][j-1]=0,0,0
            imgn[i+1][j-1]=0,0,0
            imgn[i][j]=0,0,0

#cv2.imshow('ninjas',imgn) 


for k in range(10):
    if k%1==0:
        print(round(k/10*100),"%")
    for i in range(1,h-1):
        
        
        for j in range(1,w-1):
            """
            c=1
            if j<300:
               t=0
            if j>300 and c==1:
                t=100
                c=0
            if j>301 and c==0:
                t+=j**10/10**25"""
            #for k in range(round(t)):
            b1,g1,r1=imgn[i][j]
            b2,g2,r2=imgn[i+1][j+1]
            b3,g3,r3=imgn[i+1][j-1]
            b4,g4,r4=imgn[i-1][j+1]
            b5,g5,r5=imgn[i-1][j-1]
            b6,g6,r6=imgn[i+1][j]
            b7,g7,r7=imgn[i-1][j]
            b8,g8,r8=imgn[i][j+1]
            b9,g9,r9=imgn[i][j-1]
            b1,g1,r1,b2,g2,r2=int(b1),int(g1),int(r1),int(b2),int(g2),int(r2)
            b3,g3,r3,b4,g4,r4=int(b3),int(g3),int(r3),int(b4),int(g4),int(r4)
            b5,g5,r5=int(b5),int(g5),int(r5)
            b6,g6,r6,b7,g7,r7=int(b6),int(g6),int(r6),int(b7),int(g7),int(r7)
            b8,g8,r8,b9,g9,r9=int(b8),int(g8),int(r8),int(b9),int(g9),int(r9)

            b=round((b1+b2+b3+b4+b5+b6+b7+b8+b9)/9)
            g=round((g1+g2+g3+g4+g5+g6+g7+g8+g9)/9)
            r=round((r1+r2+r3+r4+r5+r6+r7+r8+r9)/9)
            imgn[i][j]=b,g,r
            
        
cv2.imshow('ninjas',imgn)            
cv2.imwrite('newblock.png',img)    

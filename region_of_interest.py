import cv2 as cv
import numpy as np
#Region of interest

img = cv.imread("C:\\Users\\Lenovo\\Downloads\\iron-man.jpg")
img = cv.resize(img,(700,600))

# (298,7) (398,195)  ---> (x1,y1) (x2,y2)
# passing uper wale coordinate like ---> y1,y2 ---- x1,x2
roi = img[7:195,298:398]
#now find difference --->  y=188 , x = 100
img[7:195,399:499] = roi
img[7:195,500:500+100] = roi
img[7:195,298-100:298] = roi
img[7:195,298-100-100:298-100] = roi
cv.imshow('pos',img)
cv.waitKey()
cv.destroyAllWindows()

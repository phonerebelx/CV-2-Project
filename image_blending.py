import cv2 as cv
import numpy as np
#image blending
img1 = cv.imread("C:\\Users\\Lenovo\\Downloads\\iron-man.jpg")
img2 = cv.imread("C:\\Users\\Lenovo\\Downloads\\thor.jpg")
img1 = cv.resize(img1,(1024,900))
img2 = cv.resize(img2,(1024,900))
def nothing(x):
    pass

cv.namedWindow("res")
cv.createTrackbar("OFF:0,ON:1","res",0,1,nothing)
cv.createTrackbar("alpha","res",0,100,nothing)

img=np.zeros([1024,900,3],np.uint8)
while True:
    switch = cv.getTrackbarPos("OFF:0,ON:1", "res")
    alpha = cv.getTrackbarPos("alpha", "res")
    weight = float(alpha/100)
    print(weight)

    if switch == 0:
        # cv.imshow('res',np.zeros([1024,900,3] ,np.uint8))
        dst = img
    else:
        dst = cv.addWeighted(img1, 1 - weight, img2, weight, 0)

        # cv.imshow('res', np.ones([1024, 900, 3], np.uint8))
    cv.imshow("dst", dst)

    if cv.waitKey(1) == ord("q"):
        break
# cv.imshow('pos',img1)
# cv.imshow('po2s',img2)

cv.destroyAllWindows()

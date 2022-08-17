import cv2 as cv
import numpy as np

def draw(x):
    pass

img = np.zeros([700,700,3],np.uint8)


cv.namedWindow("color changer")
cv.createTrackbar("OFF:0 ON:1","color changer",0,1,draw)

cv.createTrackbar("R","color changer",0,255,draw)
cv.createTrackbar("G","color changer",0,255,draw)
cv.createTrackbar("B","color changer",0,255,draw)

while True:

    cv.imshow("color changer", img)

    if cv.waitKey(1) == ord("q"):
        break


    switch = cv.getTrackbarPos("OFF:0 ON:1","color changer")
    r = cv.getTrackbarPos("R", "color changer")
    g = cv.getTrackbarPos("G", "color changer")
    b = cv.getTrackbarPos("B", "color changer")

    if switch == 0:

        img[:] = switch

    else:

        img[:] = [r,g,b]
        print(img)

cv.destroyAllWindows()

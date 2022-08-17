import cv2 as cv
import numpy as np
def Draw(event,x,y,flags,param):
    print("events == ",event,'\n',"X == ",x,'\n',"y == ",y,'\n',"flags == ",flags,'\n',"params == ",param,'\n\n')

    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_DUPLEX
        text = 'X and Y co-ordinate ' + str(x)+str(y)
        cv.putText(cap,text,(x,y),font,1,(152,255,130),2)
    if event == cv.EVENT_RBUTTONDOWN:
        font = cv.FONT_HERSHEY_DUPLEX
        b = cap[y,x,0]
        g = cap[y,x,1]
        r = cap[y,x,2]
        text = 'BGR co-ordinate ' + str(b) +' '+ str(g) +' '+ str(r)
        cv.putText(cap,text,(x,y),font,1,(152,255,130),2)


cv.namedWindow(winname="res")

cap = cv.imread("C:\\Users\\Lenovo\\Downloads\\1186473.jpg",1)
cap = cv.resize(cap,(1500,900))
cv.setMouseCallback("res",Draw)

lst = np.array([[[ 1,2,3 ],[ 4,5,6 ],[ 7,8,9 ]]])
print(lst)
lst[:] = 0
print(lst)

# print(cap[0,0],'ls56')
print(cap)
while True:
    cv.imshow("res",cap)

    if cv.waitKey(5) & 0xFF == 27:
        break
cv.destroyAllWindows()


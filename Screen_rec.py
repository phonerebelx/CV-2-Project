import cv2 as cv
import numpy as np
# screen recorder
vidcap = cv.VideoCapture()
sc_size = pg.size()
path = "C:\\Users\\Lenovo\\Downloads\\output.mp4"

fourcc = cv.VideoWriter_fourcc(*"XVID")
output = cv.VideoWriter(path,fourcc,20.5,sc_size)

#Create window screen recording module
cv.namedWindow("Live Recording",cv.WINDOW_NORMAL)
vidcap = cv.VideoCapture(0,cv.CAP_DSHOW)
i = 0
while True:
    img = pg.screenshot()
    print(img.size)
    arr = np.array(img)
    arr = cv.cvtColor(arr,cv.COLOR_BGR2RGB)
    output.write(arr)
    cv.imshow("Live Recording",arr)
    if cv.waitKey(1) == ord("q"):
        break
    i+=1
output.release()
cv.destroyAllWindows()

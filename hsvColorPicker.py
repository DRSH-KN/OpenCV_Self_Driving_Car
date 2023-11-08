import cv2
import numpy as np

def valueChanged(value):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE MIN","HSV",0,179,valueChanged)
cv2.createTrackbar("HUE MAX","HSV",179,179,valueChanged)
cv2.createTrackbar("SAT MIN","HSV",0,255,valueChanged)
cv2.createTrackbar("SAT MAX","HSV",255,255,valueChanged)
cv2.createTrackbar("VALUE MIN","HSV",0,255,valueChanged)
cv2.createTrackbar("VALUE MAX","HSV",255,255,valueChanged)

if __name__ == "__main__":
    vid = cv2.VideoCapture('foot.mp4')
    framecount=0

    while True:
        if vid.get(cv2.CAP_PROP_FRAME_COUNT) == framecount:
            vid.set(cv2.CAP_PROP_POS_FRAMES,0)
            framecount=0
        framecount+=1
        success, frame= vid.read()

        frame = cv2.resize(frame,(480,240))
        hsvimg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("HUE MIN","HSV")
        h_max = cv2.getTrackbarPos("HUE MAX", "HSV")
        s_min = cv2.getTrackbarPos("SAT MIN","HSV")
        s_max = cv2.getTrackbarPos("SAT MAX", "HSV")
        v_min = cv2.getTrackbarPos("VALUE MIN","HSV")
        v_max = cv2.getTrackbarPos("VALUE MAX", "HSV")

        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])

        mask = cv2.inRange(hsvimg,lower, upper)
        result = cv2.bitwise_and(frame,frame, mask=mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        hstack = np.hstack([img, result, mask])

        #cv2.imshow("frame", frame)
        #cv2.imshow("hsv",frame)
        #cv2.imshow("img", img)
        cv2.imshow("mask",hstack)
        #cv2.imshow("result",result)


        key = cv2.waitKey(1)

        if key == 27:
            break
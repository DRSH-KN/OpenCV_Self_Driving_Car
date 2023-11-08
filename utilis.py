import cv2
import numpy as np

def thresholding(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    lowerWhite = np.array([80,0,160])
    upperWhite = np.array([179,255,255])
   
    whiteMask = cv2.inRange(imgHSV,lowerWhite, upperWhite)
    
    return whiteMask

def warpImg(img,points,w,h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)

    warpImg = cv2.warpPerspective(img,matrix,([w,h]))

    return warpImg

def initialiseTrackbars(initTrackbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars",360,240)
    cv2.createTrackbar("widthTop", "Trackbars",initTrackbarVals[0],wT//2, nothing)
    cv2.createTrackbar("heightTop", "Trackbars",initTrackbarVals[1],hT, nothing)
    cv2.createTrackbar("widthBottom", "Trackbars",initTrackbarVals[2],wT//2, nothing)
    cv2.createTrackbar("heightBottom","Trackbars",initTrackbarVals[3],hT,nothing)

def nothing(a):
    pass

def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("widthTop","Trackbars")
    heightTop = cv2.getTrackbarPos("heightTop","Trackbars")
    widthBottom = cv2.getTrackbarPos("widthBottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("heightBottom","Trackbars")
    points = np.float32([(widthTop,heightTop),(wT-widthTop,heightTop),(widthBottom,heightBottom),(wT-widthBottom,heightBottom)])

    return points

def drawPoints(img, points):
    for x in range(4):
        cv2.circle(img, (int(points[x][0]) , int(points[x][1])),15,(0,0,255), cv2.FILLED)
    return img

def getHistogram(img, mode=1):
    if mode ==1:
        histSum = np.sum(img, axis=0)
    else:
        histSum = np.sum(img[img.shape[0]//2: ,  :  ],axis=0)

    Threshold= 0.1*np.max(histSum)

    histArray = np.where(histSum>=Threshold)

    basepoint = int(np.average(histArray))

    return basepoint


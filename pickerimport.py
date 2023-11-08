import cv2
import numpy as np
 
img = cv2.imread("sample.png")

img = img[img.shape[0]//2: , : ]

cv2.imshow("img",img)
cv2.waitKey(0)
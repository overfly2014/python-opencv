import os
import cv2
import numpy as np

cv2.namedWindow("out",cv2.WINDOW_NORMAL)
randomData = np.random.randint(0, 255, 120000,np.uint8).reshape(100, 400, 3)
cv2.imshow("out", randomData)
cv2.waitKey()


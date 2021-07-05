import cv2
import numpy as np
import argparse
import os
import matplotlib.pyplot as plt

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Image path to the directory")
# args = vars(ap.parse_args())
# path = args['image']

path = "C:/Users/gjsdl/Desktop/kurbie.jpg"

# 입력 받은 이미지를 불러옵니다.
src = cv2.imread(path)

# hsv 컬러 형태로 변형합니다.
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h, s, v로 컬러 영상을 분리 합니다.
h, s, v = cv2.split(hsv)
# v값을 히스토그램 평활화를 합니다.
equalizedH = cv2.equalizeHist(h)
equalizedS = cv2.equalizeHist(s)
equalizedV = cv2.equalizeHist(v)
# h,s,equalizedV를 합쳐서 새로운 hsv 이미지를 만듭니다.
hsv2 = cv2.merge([h,s,equalizedV])
hsv3 = cv2.merge([h,equalizedS, equalizedV])
hsv4 = cv2.merge([equalizedH, equalizedS, equalizedV])
# 마지막으로 hsv2를 다시 BGR 형태로 변경합니다.
hsvDst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
hsvDst2 = cv2.cvtColor(hsv3, cv2.COLOR_HSV2BGR)
hsvDst3 = cv2.cvtColor(hsv4, cv2.COLOR_HSV2BGR)


cv2.imshow('imgv', cv2.vconcat([cv2.hconcat([src, hsvDst]), cv2.hconcat([hsvDst2, hsvDst3])]))

cv2.waitKey(0)
cv2.destroyAllWindows()
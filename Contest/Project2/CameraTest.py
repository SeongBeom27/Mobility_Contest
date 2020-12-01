from sys import stdin
#from jetbot import Robot
import time
import socket
from Paragon_function import mainfunc
import cv2 
import os
import time

blue_color = (255,0,0)
#robot = Robot()
image = cv2.imread('./Picture/Light_Test3Namespace().jpg')
#image = cv2.imread('./Picture/Light_Test3Namespace().jpg')
#image = cv2.imread('./Picture/solidWhiteRight.jpg')
#image = cv2.imread('./Picture/LaneDetectionTest.jpg') # 이미지 읽기
#camera = Camera.instance()
#image = camera.value

leftarr, rightarr = mainfunc(image)

#img = cv2.rectangle(image, 
img = cv2.rectangle(image, (leftarr[0,2] + 30,leftarr[0,3]), (rightarr[0,2] - 50,rightarr[0,3]), blue_color,-1)
cv2.imshow('result', img) # 결과 이미지 출력
cv2.waitKey(0)

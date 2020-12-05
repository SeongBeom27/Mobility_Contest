#from jetbot import Robot
import sys
import time
import socket
from Paragon_function import mainfunc
import cv2 
import os
import time

def CenterCalculation(left, right):
	# x1,x3   x2,x4  
	x1 = left[0,2]
	x2 = left[0,0]
	x3 = right[0,0]
	x4 = right[0,2]

	midupx = (x1 + x3)/2
	middownx = (x2 + x4)/2
	midx = (midupx + middownx)/2

	y1 = left[0,3]
	y2 = left[0,1]
	y3 = right[0,1]
	y4 = right[0,3]

	midupy = (y1 + y3)/2
	middowny = (y2 + y4)/2
	midy = (midupy + middowny)/2
	return (int(midx), int(midy))

blue_color = (255,0,0)
#robot = Robot()
image = cv2.imread('./Picture/Light_Test3Namespace().jpg')
#image = cv2.imread('./Picture/Hough_lines_img3.jpg')

#image = cv2.imread('./Picture/solidWhiteRight.jpg')
#image = cv2.imread('./Picture/LaneDetectionTest.jpg') # 이미지 읽기
#camera = Camera.instance()
#image = camera.value
'''
if image.all() == False:
	print("You couldn't read image ")
	sys.exit()
'''
leftarr, rightarr = mainfunc(image)
presentx, presenty = CenterCalculation(leftarr, rightarr)
#img = cv2.rectangle(image, 
#img = cv2.rectangle(image, (leftarr[0,2] ,leftarr[0,3]), (rightarr[0,2],rightarr[0,3]), blue_color,-1)
img = cv2.circle(image, (presentx, presenty), 5 ,blue_color,-1)
cv2.imshow('result', img) # 결과 이미지 출력
cv2.waitKey(5000)

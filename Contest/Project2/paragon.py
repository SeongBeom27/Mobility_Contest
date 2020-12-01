from sys import stdin
from jetbot import Robot
import time
import socket
from Tracing_White import mainfunc
import cv2
import os
import time

def step_forward(t):
     robot.forward(0.35)
     time.sleep(t)

def Presentlocation():
	'''
	'''
	return (x, y)

def Presentstate():
	'''
	'''
	return pimg

robot = Robot()
camera = Camera.instance()

img = cv2.rectangle(image, (

leftarr, rightarr = mainfunc(image)
img = cv2.rectangle(image, (leftarr[0,2] + 30,leftarr[0,3]), (rightarr[0,2] - 50,rightarr[0,3]), blue_color,-1)

cv2.imshow('result', img) # 결과 이미지 출력
cv2.waitKey(0)


speed = 0.33
staticx, staticy = narifunc() 							# hello
threshold = 30

stoplineflag = False												# stop line flag
obstacleflag = False

def frontLidar():
	'''
	dist calcuation
	'''
	return dist

def Start():
	while(True):
		robot.forward(speed)
        image = camera.value
		presentx, presenty = mainfunc(image)						# prsent location 
		step = 0.005
		# Using right_up, left_up
		while presentx < staticx:
			step += 0.005
			robot.right_up(speed, step)
			presentx, presenty = Presentlocation()					# Comapre present with staticlocation
		
		while presentx > staticx:
			step += 0.005
			robot.left_up(speed, step)
			presentx, presenty = Presentlocation()					# 

		step = 0.005
		# obstacle
		if !obstacleflag:
			if dist < threshold:
				obstacleflag = True
				avoid()
		
		# stop line
		if(!stoplineflag):
			if(CheckStopimg(pimg)):
				robot.stop()
				sleep(3)
				stoplineflag = True
		
		# dark light


		# strong light

		
	

if __name__ == "__main__":
	while(True):
		if(!Start()):
			break


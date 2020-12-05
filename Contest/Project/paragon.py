from jetbot import Robot
import time
import socket
from Tracing_White import mainfunc
import cv2
import os
import time

# Global vairables
robot = Robot()
camera = Camera.instance()

# leftline, rightline
leftarr, rightarr = mainfunc(image)

# Draw Rectangle which paragon will follow
img = cv2.rectangle(image, (leftarr[0,2] + 30,leftarr[0,3]), (rightarr[0,2] - 50,rightarr[0,3]), blue_color,-1)

def step_forward(t):
	robot.forward(0.35)
    time.sleep(t)

def frontLidar():
	'''
	dist calcuation
	'''
	return dist

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

	midupy = (x1 + x3)/2
	middowny = (x2 + x4)/2
	midy = (midupy + middowny)/2
	return (midx, midy)


'''
cv2.imshow('result', img) # 결과 이미지 출력
cv2.waitKey(0)
'''

speed = 0.33

staticx = 112
presentx, presenty = CenterCalculation() 
threshold = 30

stoplineflag = False												# stop line flag
obstacleflag = False


def Start():
	while(True):
        try: 
            image = camera.value
            presentx, presenty = mainfunc(image)						# prsent location 
            robot.forward(speed)
            diff = presentx - staticx
            if(abs(diff) < 5)
                robot.forward(speed)
                robot.set_motors(speed, speed)
            # Right motor up
            if(diff < 0):
                robot.set_motors(speed, speed + 0.05)
            else:
                robot.set_motors(speed + 0.05, speed)
           ''' 
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
                    '''
        except:
            camera.stop()
            return False    

if __name__ == "__main__":
	while(True):
		if(!Start()):
			break


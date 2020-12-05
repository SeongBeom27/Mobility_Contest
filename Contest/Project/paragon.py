from jetbot import Robot
from jetbot import Camera
import time
import socket
from Paragon_function import mainfunc
import cv2
import os
import time
import sys

# Global vairables
robot = Robot()
camera = Camera.instance()


# Draw Rectangle which paragon will follow
#img = cv2.rectangle(image, (leftarr[0,2] + 30,leftarr[0,3]), (rightarr[0,2] - 50,rightarr[0,3]), blue_color,-1)
'''
def step_forward(t):
	robot.forward(0.35)
    time.sleep(t)
'''
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
threshold = 30

stoplineflag = False												# stop line flag
obstacleflag = False



if __name__ == "__main__":
    print('----------------------------------------------------------------------------------------------')
    print('Race start after 3seconds')
    time.sleep(3)
    while(True):
        try:
            # leftline, rightline
            image = camera.value
            print('Load image success')
            leftarr, rightarr = mainfunc(image)
            print('Get left, right line', leftarr, rightarr)
            presentx, presenty = CenterCalculation(leftarr, rightarr) 
            print('Center x, Center y :  ', presentx, presenty)
            diff = presentx - staticx
            if abs(diff) < 5:
                print('Preseont dicrect is correct just straight')
                robot.forward(speed)
                robot.set_motors(speed, speed)
            # Right motor up
            if diff < 0:
                print('Go left!!!! Right motor up')
                robot.set_motors(speed, speed + 0.05)
            else:
                print('Go right!!!! left motor up')
                robot.set_motors(speed + 0.05, speed)
        except KeyboardInterrupt:
            print('Ctrl + C press Exit Paragon Program')
            camera.stop()
            print('----------------------------------------------------------------------------------------------')
            print('Race start after 3seconds')
            sys.exit()
        except:
            print('Non Error occur Exit Paragon Program')
            camera.stop()
            print('----------------------------------------------------------------------------------------------')
            print('Race start after 3seconds')
            sys.exit()

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

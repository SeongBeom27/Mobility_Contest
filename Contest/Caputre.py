import traitlets
import cv2
import os
import argparse
import time
from jetbot import Robot
from jetbot import Camera
from jetbot import bgr8_to_jpeg
try:
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-seq', required=False, default='1', help='Input image numbe')
	args = parser.parse_args()
	# string data

	robot = Robot()
	camera = Camera.instance()
	img = camera.value
	cv2.imwrite('./Project2/Picture/Light_Test3' + str(args.seq) + '.jpg', img)
	camera.stop()
	os._exit(1)
except:
	camera.stop()



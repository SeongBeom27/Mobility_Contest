# -*- coding: utf-8 -*- # 한글 주석쓰려면 이거 해야함
import cv2 # opencv 사용
import numpy as np

#image = cv2.imread('./Picture/Light_Test3Namespace().jpg') # 이미지 읽기

def grayscale(img): # 흑백이미지로 변환
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold): # Canny 알고리즘
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size): # 가우시안 필터
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices, color3=(255,255,255), color1=255): # ROI 셋팅

    mask = np.zeros_like(img) # mask = img와 같은 크기의 빈 이미지
    
    if len(img.shape) > 2: # Color 이미지(3채널)라면 :
        color = color3
    else: # 흑백 이미지(1채널)라면 :
        color = color1
        
    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움 
    cv2.fillPoly(mask, vertices, color)
    
    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def Line_Calculation(arr_line):
    _min = (arr_line[0,0,0] + arr_line[0,0,2])/2
    _max = (arr_line[0,0,0] + arr_line[0,0,2])/2
    leftidx = 0
    rightidx = len(arr_line) - 1
    for i in range(len(arr_line)):
        dist = (arr_line[i,0,0] + arr_line[i,0,2])/2
        if dist < _min:
	        _min = dist
	        leftidx = i
           
    for i in range(len(arr_line)):
        dist = (arr_line[i,0,0] + arr_line[i,0,2])/2
        if dist > _max:
	        _max = dist
	        rightidx = i
    target = [arr_line[leftidx,:,:], arr_line[rightidx,:,:]]
    return target 
        

	

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap): # 허프 변환
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    #line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #draw_lines(line_img, lines)

    return lines

def binarization(_img):
    return cv2.threshold(_img, 100, 255, cv2.THRESH_BINARY)
'''-----------------------------func--------------------------------------------'''
#image = cv2.imread('./Picture/LaneDetectionTest.jpg') # 이미지 읽기
#image = cv2.imread('./Picture/LanetectionTest.jpg') # 이미지 읽기	
#image = cv2.imread('./Picture/solidYellowCurve.jpg') # 이미지 읽기

#image = cv2.resize(image, dsize=(448,448), interpolation=cv2.INTER_AREA)

def mainfunc(image):
	height, width = image.shape[:2] # 이미지 높이, 너비

	gray_img = grayscale(image) # 흑백이미지로 변환
		
	gaussian_img = gaussian_blur(gray_img, 3) # Blur 효과

# binary
	ret, binary_img = binarization(gaussian_img)
#
	canny_img = canny(binary_img, 70, 210) # Canny edge 알고리즘

	vertices = np.array([[(0,height),(width/2-65, height/2+30), (width/2+100, height/2+30), (width,height)]], dtype=np.int32)
	ROI_img = region_of_interest(canny_img, vertices) # ROI 설정

	line_arr = hough_lines(ROI_img, 1, 1 * np.pi/180, 35, 15, 25) # 허프 변환
	'''
	for i in range(len(line_arr)):
		for x1,y1,x2,y2 in line_arr[i]:
			cv2.line(image, (x1, y1), (x2, y2), (0,0,255),3)
			'''
	arrline = Line_Calculation(line_arr)
	leftarr = arrline[0]
	rightarr = arrline[1]
	return (leftarr,rightarr)

'''
for i in range(len(arrline)):
    for x1,y1,x2,y2 in arrline[i]:
        cv2.line(image, (x1, y1), (x2, y2), (0,0,255),3)
		'''

#for i in range(len(arrline)):
#	for x1,y1,x2,y2 in arrline[i]:

#cv2.imshow('result', binary_img) # 결과 이미지 출력
#cv2.imshow('result', image) # 결과 이미지 출력
#cv2.waitKey(0)






import cv2
import time
import imutils
import numpy as np
# from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)

# red (hsv) :
'''
low_thr = (0,0,30)
upp_thr = (10,200,255)
'''
low_thr = (0,50,30)
upp_thr = (10,200,255)

red = [0,0,255]

import argparse

while cam.isOpened():
	ret, img = cam.read()
	#img = cv2.resize(img, (1000,1000))
	'''
	cv2.imshow('frame', img)
	cv2.waitKey(0)
	'''	
	#img = cv2.GaussianBlur(img,(7,7),7)
	#img = cv2.GaussianBlur(img,(7,7),7)
	
	# img = cv2.convertScaleAbs(img, alpha=3, beta=110)
	#'''


	img = cv2.resize(img, (360,360))

	pts1 = np.float32([[35,5],[310,10],[0,360],[360,360]])
	pts2 = np.float32([[0,0],[360,0],[0,360],[360,360]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	img = cv2.warpPerspective(img,M,(360,360))	


	gamma = 0.5
	invGamma = 1/gamma
	table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
	img = cv2.LUT(img,table)
	img = cv2.convertScaleAbs(img,alpha = 15, beta = 20)

	cv2.imshow('frame', img)
	cv2.waitKey(0)


	#'''
	'''
	gamma =	1.2
	invGamma = 1/gamma
	table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
	img = cv2.LUT(img,table)
	img = cv2.convertScaleAbs(img,alpha = 4)
	'''


	frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(frame, low_thr, upp_thr)
	
	
	blur1 = cv2.GaussianBlur(mask,(7,7),7)
	blur1 = cv2.resize(blur1, (200,200))
	
	for i in range(2):
		for j in range(200):
			for k in range(200):
					blur1[j,k] = (255 if (blur1[j,k] > 20) else 0)
		blur1 = cv2.GaussianBlur(blur1,(7,7),7)
	
	cam.release()
	'''
	cv2.imshow('frame', img)
	cv2.waitKey(0)
	cv2.imshow('frame', frame)
	cv2.waitKey(0)
	cv2.imshow('frame', mask)
	cv2.waitKey(0)
	'''
	# cv2.imshow('frame', blur1)
	# cv2.waitKey(0)
	
	blur1 = cv2.resize(blur1, (360,360))


	# cv2.imshow('frame', blur1)
	# cv2.waitKey(0)

	dst = blur1

	cv2.imshow('frame', dst)
	cv2.waitKey(0)

	grid = []
	for i in range(9):
		grid.append([])
		for j in range(9):
			grid[i].append(1 if ((dst[(20+(i*40)),(20+(j*40))])!=0) else 0)
	for i in range(9):
		print(grid[i])





cv2.destroyAllWindows()



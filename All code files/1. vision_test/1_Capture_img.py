'''
import cv2
import numpy as np
cap=cv2.VideoCapture('fswebcam')
while(1):
	ret,img=cap.read()
	cv2.imshow('frame',img)
	cv2.imwrite('save1.jpg',img)
	cv2.waitKey(0)
	break
cap.release()
cv2.destroyAllWindows()
'''

import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
i=0
while(i<200):
	cap.release()
	cap = cv2.VideoCapture(0)
	ret, img = cap.read()
	cap.release()
	cv2.imshow('frame', img)
	'''
	cv2.imwrite('test_canny.jpg',img)
	img = cv2.imread('test_canny.jpg',0)
	edges = cv2.Canny(img,100,200)
	plt.subplot(121),plt.imshow(img,cmap = 'gray')
	plt.title('Original Image'),plt.xticks([]),plt.yticks([])
	plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'),plt.xticks([]),plt.yticks([])
	plt.show()
	time.sleep(3)
	'''
	cv2.waitKey(300)
	cv2.destroyAllWindows()
	i+=1

cap.release()
cv2.destroyAllWindows()



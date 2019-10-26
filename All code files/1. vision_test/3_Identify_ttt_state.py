
import cv2
import numpy as np

def get_board_state():
	cam = cv2.VideoCapture(0)
	ret, img = cam.read()
	cam.release()
	gamma = 0.5
	invGamma = 1/gamma
	table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
	img = cv2.LUT(img,table)
	img = cv2.convertScaleAbs(img,alpha = 10,beta=20)
	frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	low_thr = (0,50,30)
	upp_thr = (10,200,255)
	mask = cv2.inRange(frame, low_thr, upp_thr)
	bluredImg = cv2.GaussianBlur(mask,(7,7),7)
	bluredImg = cv2.resize(bluredImg, (200,200))
	for i in range(2):
		for j in range(200):
			for k in range(200):
					bluredImg[j,k] = (255 if (bluredImg[j,k] > 0) else 0)
		bluredImg = cv2.GaussianBlur(bluredImg,(7,7),7)
	bluredImg = cv2.resize(bluredImg, (360,360))
	pts1 = np.float32([[36,0],[324,10],[10,350],[360,360]])
	pts2 = np.float32([[0,0],[360,0],[0,360],[360,360]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	dst = cv2.warpPerspective(bluredImg,M,(360,360))
	grid = []
	for i in range(9):
		grid.append([])
		for j in range(9):
			grid[i].append(1 if ((dst[(20+(i*40)),(20+(j*40))])!=0) else 0)
	cv2.destroyAllWindows()
	return np.array(grid)

def update_board_state(prev_state, glb_box):
	[row_no,col_no] = glb_box
	curr_board_state = get_board_state()
	mask = []
	for i in range(9):
		mask.append([])
		for j in range(9):
			mask[i].append(1 if ((i//3==row_no) and (j//3==col_no) and (prev_state[i,j]==0)) else 0)
	mask = np.array(mask)
	curr_board_state = np.array(curr_board_state)
	updated_board = prev_state+(curr_board_state*mask)
	diff = updated_board - prev_state
	nxt_glb = -1
	for i in range(3*row_no,3*(1+row_no)):
		for j in range(3*col_no,3*(1+col_no)):
			if diff[i,j]==1:
				nxt_glb = (i%3,j%3)
				break
		if (nxt_glb!=-1):
			break
	return updated_board,nxt_glb


def mainfunction():
	l = get_board_state()
	for i in range(9):
		print(l[i])
	prev_state = l
	input()
	l, g = update_board_state(prev_state, (2,1))
	for i in range(9):
		print(l[i])
	print(g)

'''
def mainfunction1():
	curr_state = play_first()
	while(!is_endgame(curr_state)):
		# delay(1000)
		input()
		nxt_ind = is_vacant()
		board, glb = update_board_state(curr_state, glb_nxt)
		if nxt_ind!=-1 and glb!=-1 :
			curr_state = board
			glb_next = glb
		for i in range(9):
			print(l[i])
		print(g)
		curr_state = play_turn()
'''
def debugfunction():
	l = get_board_state()
	for i in range(9):
		print(l[i])

# mainfunction()
debugfunction()








import random
import cv2
import numpy as np

def get_board_state():
	cam = cv2.VideoCapture(0)
	ret, img = cam.read()
	cam.release()
	img = cv2.resize(img, (360,360))
	pts1 = np.float32([[35,5],[310,10],[0,360],[360,360]])
	pts2 = np.float32([[0,0],[360,0],[0,360],[360,360]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	img = cv2.warpPerspective(img,M,(360,360))
	gamma = 0.5
	invGamma = 1/gamma
	table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
	img = cv2.LUT(img,table)
	img = cv2.convertScaleAbs(img,alpha = 10, beta = 20)
	# cv2.imshow('frame', img)
	# cv2.waitKey(0)
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
	dst = bluredImg
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

def my_turn(curr_state, glb_nxt):
	[row_no,col_no] = glb_nxt

	'''
	empty_sq_lst = []
	for i in range(3*row_no,3*(1+row_no)):
		for j in range(3*col_no,3*(1+col_no)):
			if curr_state[i,j]==0:
				empty_sq_lst.append((i,j))
	play_at = random.randint(0,len(empty_sq_lst)-1)
	play_at = empty_sq_lst[play_at]
	'''

	# '''
	mini_board = []
	for i in range(3*row_no,3*(1+row_no)):
		for j in range(3*col_no,3*(1+col_no)):
			mini_board.append(curr_state[i,j])
	ply = comp_mov(mini_board)
	i = ply//3
	j = ply%3
	play_at = (i+(3*row_no),j+(3*col_no))
	# '''

	print "played at : "
	print play_at
	play_at_i = play_at[0]
	play_at_j = play_at[1]
	curr_state[play_at_i,play_at_j] = -1
	nxt_glb = (play_at_i%3,play_at_j%3)
	return curr_state,nxt_glb


def your_turn(curr_state, glb_nxt):
	input("your Turn : ")
	return update_board_state(curr_state, glb_nxt)


def debugfunction():
	l = get_board_state()
	l[2,2] = -1
	l[2,6] = -1
	l[3,5] = -1
	l[6,0] = -1
	l[6,6] = -1
	l[7,5] = -1
	l[1,3] = -1
	l[2,0] = -1
	l[0,6] = -1
	l[1,8] = -1
	l[6,3] = -1
	l[0,3] = -1
	l[5,4] = -1
	l[0,5] = -1
	l[4,3] = -1
	l[8,5] = -1
	l[8,3] = -1
	l[8,6] = -1
	l[0,4] = -1
	l[4,7] = -1
	l[1,4] = -1
	l[7,6] = -1
	l[1,6] = -1
	l[7,1] = -1
	l[5,6] = -1
	l[3,8] = -1
	# for i in range(9):
	# 	print(l[i])
	curr_state = l
	glb_nxt = (2,1)
	print
	print
	while(True):
		print
		curr_state,glb_nxt = my_turn(curr_state, glb_nxt)
		print
		curr_state,glb_nxt = your_turn(curr_state, glb_nxt)
	



def comp_mov(board):
	for i in range(9):
		copy = copyBoard(board)
		if copy[i]==0:
			copy[i] = -1
			if isWinner(copy, -1):
				return i
	for i in range(9):
		copy = copyBoard(board)
		if copy[i]==0:
			copy[i] = 1
			if isWinner(copy, 1):
				return i
	l = [0,2,6,8]
	move = chooseRand(board,l)
	if move!=-1:
		return move
	if board[4]==0:
		return 4
	l = [1,3,5,7]
	move = chooseRand(board,l)
	if move!=-1:
		return move

def isWinner(bo, le):
	return( (bo[0]==le and bo[1]==le and bo[2]==le) or 
		 (bo[3]==le and bo[4]==le and bo[5]==le) or 
		 (bo[6]==le and bo[7]==le and bo[8]==le) or 
		 (bo[0]==le and bo[3]==le and bo[6]==le) or 
		 (bo[1]==le and bo[4]==le and bo[7]==le) or 
		 (bo[2]==le and bo[5]==le and bo[8]==le) or 
		 (bo[0]==le and bo[4]==le and bo[8]==le) or 
		 (bo[2]==le and bo[4]==le and bo[6]==le) )

def copyBoard(board):
	cb = []
	for i in board:
		cb.append(i)
	return cb

def chooseRand(bo,l):
	poss = []
	for i in l:
		if bo[i]==0:
			poss.append(i)
	if len(poss)!=0:
		return random.choice(poss)
	else:
		return -1









# mainfunction()
debugfunction()



































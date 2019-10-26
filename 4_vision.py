import random
import time
import cv2
import numpy as np



import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin

def set_zero(servos):
	for i in range(3, 0, -1):
		wp.softPwmWrite(servos[i],0)
		wp.delay(200)


def main_go_arm(val):
	(l,b,r) = val
	servo_list = [0,24,18,23]
	servos = [0, Servo(servo_list[1]),  Servo(servo_list[2]), Servo(servo_list[3])]
	
	val_list = [0,15,4,9]
	for i in range(3, 0, -1):
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(500)
	set_zero(servos)
	wp.delay(2000)
	val_list[1] = 31
	
	wp.softPwmWrite(servos[1],31)
	wp.delay(500)
	set_zero(servos)
	wp.delay(2000)
	val_list[2] = b
	wp.softPwmWrite(servos[2],b)
	wp.delay(500)
	set_zero(servos)
	'''
	diff1 = val_list[1]-l
	diff2 = val_list[3]-r
	total_diff = abs(abs(diff1)-abs(diff2))
	if (diff1!=0):
		s1 = diff1//abs(diff1)
	else :
		s1= 0
	if (diff2!=0):
		s2 = diff2//abs(diff2)
	else :
		s2= 0
	'''
	#print(val_list)

	wp.softPwmWrite(servos[1],l)
	wp.delay(500)
	wp.softPwmWrite(servos[3],r)
	wp.delay(4000)
	wp.softPwmWrite(servos[1],31)
	wp.delay(500)
	set_zero(servos)


	wp.delay(500)
	val_list = [0,15,4,9]
	for i in range(3, 0, -1):
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(500)
	set_zero(servos)

def get_board_state():
	cam = cv2.VideoCapture(0)
	ret, img = cam.read()
	cam.release()
	img = cv2.resize(img, (360,360))
	pts1 = np.float32([[35,5],[310,10],[0,360],[360,360]])
	pts2 = np.float32([[0,0],[360,0],[0,360],[360,360]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	img = cv2.warpPerspective(img,M,(360,360))
	'''
	gamma = 0.5
	invGamma = 1/gamma
	table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
	img = cv2.LUT(img,table)
	img = cv2.convertScaleAbs(img,alpha = 10, beta = 20)
	'''
	'''cv2.imshow('frame', img)
	cv2.waitKey(0)'''
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
	for i in range(3):
		grid.append([])
		for j in range(3):
			grid[i].append(1 if ((dst[(60+(i*120)),(60+(j*120))])!=0) else 0)
	cv2.destroyAllWindows()
	return np.array(grid)

def isDiff(diff):
	[row_no,col_no] = (0,0)
	cnt = 0
	for i in range(3*row_no,3*(1+row_no)):
		for j in range(3*col_no,3*(1+col_no)):
			if diff[i,j]==1:
				cnt+=1
	if cnt!=1:
		return -1
	else:
		return 1

def update_board_state(prev_state):
	[row_no,col_no] = (0,0)

	curr_board_state = get_board_state()
	mask = []
	for i in range(3):
		mask.append([])
		for j in range(3):
			mask[i].append(1 if ((i//3==row_no) and (j//3==col_no) and (prev_state[i,j]==0)) else 0)
	mask = np.array(mask)
	curr_board_state = np.array(curr_board_state)
	updated_board = prev_state+(curr_board_state*mask)
	diff = updated_board - prev_state
	isDifferent = isDiff(diff)
	if isDifferent==-1:
		return -1
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

def my_turn(curr_state):
	[row_no,col_no] = (0,0)

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

	print "I played at : "
	print play_at
	move_arm_to(play_at)
	play_at_i = play_at[0]
	play_at_j = play_at[1]
	curr_state[play_at_i,play_at_j] = -1
	nxt_glb = (play_at_i%3,play_at_j%3)
	return curr_state,nxt_glb


def your_turn(curr_state):
	op = -1
	print
	while (op==-1):
		print ("Waiting....")
		time.sleep(3)
		op = update_board_state(curr_state)
		# print op
	return op


def debugfunction():
	print
	curr_state = np.zeros((9,9), dtype=int)
	glb_nxt = (1,1)
	print
	print "MY TURN FIRST !!"
	print
	curr_state,glb_nxt = my_turn(curr_state, glb_nxt)
	print
	print
	while(True):

		f = open("GAME_STATE", "w+")
		f.write("your_turn next \n" + str(curr_state) + "\n" +str(glb_nxt))
		f.close()
		
		print
		print "YOUR TURN"
		

		curr_state,glb_nxt = your_turn(curr_state, glb_nxt)
		
		print

		print "MY TURN"
		print
		print "Thinking...."

		curr_state,glb_nxt = my_turn(curr_state, glb_nxt)
	



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


def isDraw(bo):
	for i in bo:
		if i==0:
			return 0
	return 1


def move_arm_to(play_at):
	pt = 3*play_at[0]+play_at[1]
	lt = [[18,11,14],[16,11,13],[14,10,10],[18,13,14],[16,13,13],[14,13,10],[19,14,15],[16,15,13],[13,16,9]]
	main_go_arm(lt[pt])



def func1():
	'''
	print
	curr_state = np.zeros((9,9), dtype=int)
	glb_nxt = (1,1)
	print
	print "MY TURN FIRST !!"
	print
	curr_state,glb_nxt = my_turn(curr_state, glb_nxt)
	print
	print
	'''
	curr_state =[[0,0,0],[0,0,0],[0,0,0]]
	curr_state = np.array(curr_state)

	while(True):

		
		print
		print "YOUR TURN"
		

		curr_state,glb_nxt = your_turn(curr_state)
		
		
		copy = []
		for i in range(3):
			for j in range(3):
				copy.append(curr_state[i,j])


		if isWinner(copy, 1):
			print "you WIN"
			exit(0)

		if isDraw(copy):
			print "DRAW"
			exit(0)

		print

		print "MY TURN"
		print
		print "Thinking...."

		curr_state,glb_nxt = my_turn(curr_state)
	

		copy = []
		for i in range(3):
			for j in range(3):
				copy.append(curr_state[i,j])

		if isWinner(copy, -1):
			print "I WIN"
			exit(0)
		
		if isDraw(copy):
			print "DRAW"
			exit(0)

		print curr_state

# mainfunction()
# debugfunction()
func1()




































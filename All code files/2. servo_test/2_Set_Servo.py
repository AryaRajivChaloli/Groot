'''
import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin

def set_zero():
	servo_list = [0,24,18,23]
	#  : left
	#  : base
	#  : right
	
	val_list = [0,0,0,0]#[0,21,21,5]
	
	servo = Servo(servo_list[1])
	wp.softPwmWrite(servo,val_list[1])
	wp.delay(200)
	
	servo = Servo(servo_list[3])
	wp.softPwmWrite(servo,val_list[3])
	wp.delay(200)
	
	servo = Servo(servo_list[2])
	wp.softPwmWrite(servo,val_list[2])
	wp.delay(200)

def main():
	
	servo_list = [0,24,18,23]
	#  : left
	#  : base
	#  : right
	
	val_list = [0,21,21,5]
	
	servo = Servo(servo_list[1])
	wp.softPwmWrite(servo,val_list[1])
	wp.delay(200)
	
	servo = Servo(servo_list[3])
	wp.softPwmWrite(servo,val_list[3])
	wp.delay(200)
	
	servo = Servo(servo_list[2])
	wp.softPwmWrite(servo,val_list[2])
	wp.delay(200)
	
	set_zero()
	
	ctrl = 2
	# 1 : left
	# 2 : base
	# 3 : right

	while True:
		inp = input('Value : ')
		if (inp==1):
			print 'left'
			ctrl = 1
			servo = Servo(servo_list[ctrl])
		elif (inp==2):
			print 'base'
			ctrl = 2
			servo = Servo(servo_list[ctrl])
		elif (inp==3):
			print 'right'
			ctrl = 3
			servo = Servo(servo_list[ctrl])
		elif (inp==8):
			val_list[ctrl] = val_list[ctrl] - 1
			wp.softPwmWrite(servo,val_list[ctrl])
			wp.delay(200)
		elif (inp==9):
			val_list[ctrl] = val_list[ctrl] + 1
			wp.softPwmWrite(servo,val_list[ctrl])
			wp.delay(200)
		elif (inp==5):
			print val_list[1:]
		set_zero()


if __name__=='__main__':
	main()
'''
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

def go_to(servos,val_list):
	for i in [1,2,3]:
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(500)

def main():
	
	servo_list = [0,24,18,23]
	servos = [0, Servo(servo_list[1]),  Servo(servo_list[2]), Servo(servo_list[3])]
	#  : left
	#  : base
	#  : right
	
	val_list = [0,21,21,5]
	
	for i in range(3, 0, -1):
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(500)
	
	set_zero(servos)
	
	ctrl = 2
	# 1 : left
	# 2 : base
	# 3 : right

	while True:
		inp = input('Value : ')
		if (inp==1):
			print 'left'
			ctrl = 1
		elif (inp==2):
			print 'base'
			ctrl = 2
		elif (inp==3):
			print 'right'
			ctrl = 3
		elif (inp==8):
			val_list[ctrl] = val_list[ctrl] - 1
			wp.softPwmWrite(servos[ctrl],val_list[ctrl])
			wp.delay(200)
		elif (inp==9):
			val_list[ctrl] = val_list[ctrl] + 1
			wp.softPwmWrite(servos[ctrl],val_list[ctrl])
			wp.delay(200)
		elif (inp==5):
			print val_list[1:]
		elif (inp==6):
			val_list = [0,31,13,7] #mid
			go_to(servos,val_list)
		elif (inp==7):
			val_list = [0,21,21,5] #reset
			go_to(servos,val_list)
		elif (inp==4):
			val_list = [0,input('l:'),input('b:'),input('r:')]
			go_to(servos,val_list)
		set_zero(servos)


if __name__=='__main__':
	main()




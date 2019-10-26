
# base
import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin
def Position(servo,pos):
	(pin)=servo
	wp.softPwmWrite(pin,pos)
def Sweep(servo,delay, st,ed):
	pin=servo
	for i in range(st,ed+1,1):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
	wp.delay(2000)
	'''
	for i in range(ed,st-1,-1):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
	'''
if __name__=='__main__':
	'''
	l = 4
	wp.softPwmWrite(servo1,l)
	wp.delay(2000)
	input('key :')
	#wp.softPwmWrite(servo1,1)
	# wp.delay(2000)
	# input('key :')
	for i in range(4):
		Sweep(servo1,40,(5*i),(5*(i+1)))
		input('key :')
	'''
	
	servo1=Servo(24)
	ser = Servo(18)
	servo=Servo(23)
	'''
	cnt = 0
	l = []
	#input('key :')
	for k in range(1):
		wp.softPwmWrite(servo,15)
		wp.delay(200)
		wp.softPwmWrite(servo,0)
		wp.delay(200)
		wp.softPwmWrite(servo1,14)
		wp.delay(200)
		wp.softPwmWrite(servo1,0)
		wp.delay(200)

		wp.softPwmWrite(ser,8+k)
		wp.delay(200)
		wp.softPwmWrite(ser,0)
		wp.delay(2000)
		for j in range(1,10):
			print cnt
			s = 15
			wp.softPwmWrite(servo,8)
			wp.delay(200)
			wp.softPwmWrite(servo,0)
			wp.delay(200)
			wp.softPwmWrite(servo1,14)
			wp.delay(200)
			wp.softPwmWrite(servo1,0)
			wp.delay(200)
			s1 =  14
			for i in range(j):
				wp.softPwmWrite(servo,s)
				wp.delay(40)
				wp.softPwmWrite(servo,0)
				wp.delay(40)
				wp.softPwmWrite(servo1,s1)
				wp.delay(40)
				wp.softPwmWrite(servo1,0)
				wp.delay(40)
				s=s+1
				if i>=8:
					s1+=8
				elif i>=4:
					s1+=2
				elif i>=7:
					s1+=4
				else:
					s1=s1+1
			l.append([s1,8+k,s])
			cnt+=1
	print l

	

	'''	# CORRECT
	cnt = 0
	l = []
	#input('key :')
	for k in range(1):
		wp.softPwmWrite(servo,14)
		wp.delay(200)
		wp.softPwmWrite(servo,0)
		wp.delay(200)
		wp.softPwmWrite(servo1,14)
		wp.delay(200)
		wp.softPwmWrite(servo1,0)
		wp.delay(200)

		wp.softPwmWrite(ser,8+k)
		wp.delay(200)
		wp.softPwmWrite(ser,0)
		wp.delay(2000)
		for j in range(1,10):
			print cnt
			cnt+=1
			s = 14
			s1 =  14
			for i in range(j):
				wp.softPwmWrite(servo,s)
				wp.delay(40)
				wp.softPwmWrite(servo,0)
				wp.delay(40)
				wp.softPwmWrite(servo1,s1)
				wp.delay(40)
				wp.softPwmWrite(servo1,0)
				wp.delay(40)
				s=s+1
				if i>=8:
					s1+=8
				elif i>=4:
					s1+=2
				elif i>=7:
					s1+=4
				else:
					s1=s1+1
			wp.delay(000)
	




































	'''
		wp.softPwmWrite(servo1,s1-5)
		wp.delay(40)
		wp.softPwmWrite(servo1,0)
		wp.delay(40)
		wp.delay(5000)
	'''# input('key :')
	



'''
# lft
import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin
def Position(servo,pos):
	(pin)=servo
	wp.softPwmWrite(pin,pos)
def Sweep(servo,delay, st,ed):
	pin=servo
	for i in range(st,ed-1,-1):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
	wp.delay(2000)
	
	for i in range(ed,st+1,1):
		wp.softPwmWrite(pin,i)
		wp.delay(10)
	wp.delay(2000)
	
if __name__=='__main__':
	servo1=Servo(18)
	
	for i in range(15,61,1):
		wp.softPwmWrite(servo1,i)
		wp.delay(10)
	wp.delay(2000)
	
	# Sweep(servo1,30,60,15)
'''
'''
# rgt
import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin
def Position(servo,pos):
	(pin)=servo
	wp.softPwmWrite(pin,pos)
def Sweep(servo,delay, st,ed):
	pin=servo
	for i in range(st,ed+1,1):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
	wp.delay(2000)
	for i in range(ed,st-1,-1):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
if __name__=='__main__':
	servo1=Servo(18)


	Sweep(servo1,40,10,15)
'''

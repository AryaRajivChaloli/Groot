list_of_points = [[15, 8, 9], [16, 8, 10], [17, 8, 11], [18, 8, 12], [20, 8, 13], [22, 8, 14], [24, 8, 15], [26, 8, 16], [34, 8, 17], [15, 9, 9], [16, 9, 10], [17, 9, 11], [18, 9, 12], [20, 9, 13], [22, 9, 14], [24, 9, 15], [26, 9, 16], [34, 9, 17], [15, 10, 9], [16, 10, 10], [17, 10, 11], [18, 10, 12], [20, 10, 13], [22, 10, 14], [24, 10, 15], [26, 10, 16], [34, 10, 17], [15, 11, 9], [16, 11, 10], [17, 11, 11], [18, 11, 12], [20, 11, 13], [22, 11, 14], [24, 11, 15], [26, 11, 16], [34, 11, 17], [15, 12, 9], [16, 12, 10], [17, 12, 11], [18, 12, 12], [20, 12, 13], [22, 12, 14], [24, 12, 15], [26, 12, 16], [34, 12, 17], [15, 13, 9], [16, 13, 10], [17, 13, 11], [18, 13, 12], [20, 13, 13], [22, 13, 14], [24, 13, 15], [26, 13, 16], [34, 13, 17], [15, 14, 9], [16, 14, 10], [17, 14, 11], [18, 14, 12], [20, 14, 13], [22, 14, 14], [24, 14, 15], [26, 14, 16], [34, 14, 17], [15, 15, 9], [16, 15, 10], [17, 15, 11], [18, 15, 12], [20, 15, 13], [22, 15, 14], [24, 15, 15], [26, 15, 16], [34, 15, 17], [15, 16, 9], [16, 16, 10], [17, 16, 11], [18, 16, 12], [20, 16, 13], [22, 16, 14], [24, 16, 15], [26, 16, 16], [34, 16, 17]]


import wiringpi as wp
wp.wiringPiSetupGpio()
def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin

def set_zero(servos):
	for i in [2,3,1]:
		wp.softPwmWrite(servos[i],0)
		wp.delay(200)

def go_to(servos,val_list):
	for i in [2,3,1]:
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(2000)
def go_back(servos,val_list):
	for i in [3,1,2]:
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(2000)

def main():
	
	servo_list = [0,24,18,23]
	servos = [0, Servo(servo_list[1]),  Servo(servo_list[2]), Servo(servo_list[3])]
	#  : left
	#  : base
	#  : right
	
	val_list = [0,21,21,5]
	
	for i in [2,3,1]:
		wp.softPwmWrite(servos[i],val_list[i])
		wp.delay(500)
	
	set_zero(servos)
	

	while True:
		inp = list_of_points[int(input('Goto : '))]

		val_list = [0,21,21,5] #reset
		go_to(servos,val_list)

		set_zero(servos)
		wp.delay(2000)

		val_list = [0,31,13,4] #mid
		go_to(servos,val_list)

		set_zero(servos)
		wp.delay(2000)
		input()

		val_list = [0]
		val_list.extend(inp)
		go_to(servos,val_list)

		set_zero(servos)
		wp.delay(2000)

		val_list = [0,31,13,4] #mid
		go_back(servos,val_list)

		set_zero(servos)
		wp.delay(2000)

		val_list = [0,21,21,5] #reset
		go_to(servos,val_list)

		set_zero(servos)
		wp.delay(2000)


if __name__=='__main__':
	main()


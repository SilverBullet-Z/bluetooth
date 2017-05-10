#coding=utf-8

'''
Fun_us.py 超声波（Ultrasonic）测距程序

'''

import RPi.GPIO as GPIO
import time

def checkdist(op,ip):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(op,GPIO.OUT)
	GPIO.setup(ip,GPIO.IN)
	n=2#发射次数
	k=0
	for i in range(n):
		#发出触发信号
		GPIO.output(op,1)
		time.sleep(0.2)
		GPIO.output(op,0)
		while  not GPIO.input(ip):
			pass
		#发现高电平时开时计时
		t1 = time.time()
		while GPIO.input(ip):
			pass
		t2 = time.time()
		#返回距离
		ds=(t2-t1)*34300/2
		k+=ds
	k=k//n
	print 'Distance: %0.2f m' % k
	return k

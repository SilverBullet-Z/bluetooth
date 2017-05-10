#coding=utf-8

'''
Fun_se.py 舵机（steering engine）程序

'''

import RPi.GPIO as GPIO
import time

servopin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT, initial=False)
# 设置 PWM 信号频率 50Hz
p = GPIO.PWM(servopin,50) 
p.start(0)
time.sleep(2)

def turn(deg1,deg2):
	i=deg1
	if i<=deg2:		
		while i<=deg2:
			p.ChangeDutyCycle(2.5 + 10 * i / 180) # 设置舵机角度
			time.sleep(0.02)
			p.ChangeDutyCycle(0) # 舵机回到中位
			time.sleep(0.2)
			i+=10
		while i>=deg2:
			p.ChangeDutyCycle(2.5 + 10 * i / 180)
			time.sleep(0.02)
			p.ChangeDutyCycle(0)
			time.sleep(0.2)
			k-=10
	
			
#coding=utf-8

'''
Fun_pwm_moto.py pwm调速程序

'''

import RPi.GPIO as GPIO
import time

#使能和速度设置

gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)

pr=gpio.PWM(12,50); pr.start(92)
pl=gpio.PWM(16,50); pl.start(100)


p.start(dc)

def max():
	while dc:
		dc += 1
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)

def min():
	while dc:
		dc -= 1
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)

p.stop()
GPIO.cleanup()
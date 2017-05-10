# -*- coding: utf-8 -*-
import bluetooth
import threading
#import redis

import RPi.GPIO as gpio
import time
import sys
import Run_mt_moto
import Run_auto_moto
import Mode_auto_ir
import Mode_auto_us


#服务器套接字(用来接收新链接)
server_socket=None

#连接套接字服务子线程
def serveSocket(sock,info):
	#开个死循环等待客户端发送信息
	while True:
		#接收1024个字节,然后以UTF-8解码(中文),如果没有可以接收的信息则自动阻塞线程(API)
		receive=sock.recv(1024).decode('utf-8');
		#r=redis.Redis(host='127.0.0.1',port=6379)
		#r.set('status',receive)
		#打印刚刚读到的东西(info=地址)
		print('['+str(info)+']'+receive);
		#指令判断
		while True:

			if receive  == 'w':
				Run_mt_moto.Car.fowd()
				sock.send('forward...')
				break
			elif receive  == 'a':
				Run_mt_moto.Car.left()
				sock.send('left...')
				break
			elif receive == 's':
				Run_mt_moto.Car.back()
				sock.send('back...')
				break
			elif receive == 'd':
				Run_mt_moto.Car.right()
				sock.send('right...')
				break
			elif receive == 'p':
				Run_mt_moto.Car.stop()
				sock.send('stop...')
				break
			elif receive == 'us':
				Mode_auto_us.us(1)
				sock.send('ir...')
				break
			elif receive == 'uo':
				Mode_auto_us.uo(0)
				sock.send('uo...')
				break
			elif receive == 'ir':
				Mode_auto_ir.ir(1)
				sock.send('ir...')
				break
			elif receive == 'io':
				Mode_auto_ir.ir(0)
				sock.send('io...')
				break
			elif receive == 'tm':
				time.sleep(0.05)
				sock.send('delay...')
				break
			elif receive == 'q':
				sock.send('now exit...')
				gpio.cleanup()
				time.sleep(0.05)
				sys.exit(0)
			
		'''
		#为了返回好看点,加个换行
		receive=receive+"\n";
		#回传数据给发送者
		sock.send(receive.encode('utf-8'));
		'''

#主线程

#创建一个服务器套接字,用来监听端口
server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM);
#允许任何地址的主机连接,未知参数:(端口号,通道号)
try:
	channel = 1
	server_socket.bind(("",channel))
except Exception, e:
	channel+=1
	server_socket.bind(("",channel))

#监听端口/通道
server_socket.listen(channel);

#开死循环 等待客户端连接
#本处应放在另外的子线程中
try:
	while True:
		#等待有人来连接,如果没人来,就阻塞线程等待(这本来要搞个会话池,以方便给不同的设备发送数据)
		sock,info=server_socket.accept();
		#打印有人来了的消息
		print(str(info[0])+' Connected!');
		#创建一个线程专门服务新来的连接(这本来应该搞个线程池来管理线程的)
		t=threading.Thread(target=serveSocket,args=(sock,info[0]))
		#设置线程守护,防止程序在线程结束前结束
		t.setDaemon(True)
		#启动线程
		t.start();
except KeyboardInterrupt:
	pass

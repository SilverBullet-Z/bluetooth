#coding=utf-8

'''
Mode_auto_ir.py 智能小车红外避障主模块
'''

import RPi.GPIO as GPIO
import time
import Run_auto_moto
#import Run_pwm_moto 
#import sys
import redis

#主程序


LL = 21
LR = 22
RL = 23
RR = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LL,GPIO.IN)
GPIO.setup(LR,GPIO.IN)
GPIO.setup(RL,GPIO.IN)
GPIO.setup(RR,GPIO.IN)


def ir(wd):
        try:
                pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
                r = redis.Redis(connection_pool=pool)

                while True:
                        if wd == 0 :
                                print "Now you exit the Auto_us MODE"
                                Com_bluetooth(sock,info)
                                GPIO.cleanup()
                                
                        elif wd== 1:
                                print "Now the Auto_ir MODE is running"
                                while True:

                                        BLL = GPIO.input(LL)
                                        BLR = GPIO.input(LR)
                                        BRL = GPIO.input(RL)
                                        BRR = GPIO.input(RR)
                                        #print ("com"+r.get('status'))
                                        if r.get('status') == 'uo':
                                                print ("com2"+r.get('status'))
                                                time.sleep(0.3)
                                                print "exit ir..."
                                                GPIO.cleanup()
                                                Com_bluetooth(sock,info)
                                        elif BLL == True and BLR == True and BRL == True and BRR == True:
                                                Run_auto_moto.Car.back()
                                                print "1"
                                                
                                        elif BLL == False and BLR == True and BRL == True and BRR == True:
                                                Run_auto_moto.Car.right()
                                                print "2"
                                                
                                        elif BLL == True and BLR == False and BRL == True and BRR == True:
                                                Run_auto_moto.Car.right()
                                                print "3"
                                                               
                                        elif BLL == True and BLR == True and BRL == False and BRR == True:
                                                Run_auto_moto.Car.left()
                                                print "4"
                                                
                                        elif BLL == True and BLR == True and BRL == True and BRR == False:
                                                Run_auto_moto.Car.left()
                                                print "5"
                                                
                                        elif BLL == False and BLR == False and BRL == True and BRR == True:
                                                Run_auto_moto.Car.right()
                                                print "6"
                                                
                                        elif BLL == False and BLR == True and BRL == False and BRR == True:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.left()
                                                time.sleep(0.3)
                                                print "7"
                                                                           
                                        elif BLL == False and BLR == True and BRL == True and BRR == False:
                                                Run_auto_moto.Car.back()
                                                print "8"
                                                
                                        elif BLL == True and BLR == False and BRL == False and BRR == True:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.left()
                                                time.sleep(0.3)
                                                print "9"
                                                                       
                                        elif BLL == True and BLR == False and BRL == True and BRR == False:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.left()
                                                time.sleep(0.3)
                                                print "10"
                                                                        
                                        elif BLL == True and BLR == True and BRL == False and BRR == False:
                                                Run_auto_moto.Car.left()
                                                print "11"
                                                                     
                                        elif BLL == False and BLR == False and BRL == False and BRR == True:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.right()
                                                time.sleep(0.3)
                                                print "12"
                                                                        
                                        elif BLL == False and BLR == False and BRL == True and BRR == False:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.right()
                                                time.sleep(0.3)
                                                print "13"
                                                
                                        elif BLL == False and BLR == True and BRL == False and BRR == False:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.left()
                                                time.sleep(0.3)
                                                print "14"
                                                
                                        elif BLL == True and BLR == False and BRL == False and BRR == False:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.left()
                                                time.sleep(0.3)
                                                print "15"
                                                
                                        elif BLL == False and BLR == False and BRL == False and BRR == False:
                                                Run_auto_moto.Car.fowd()
                                                time.sleep(0.4)
                                                Run_auto_moto.Car.right()
                                                time.sleep(0.3)
                                                print "16"
                                                


                                
        except Exception, e:
                print "Now you exit the Auto_ir MODE"
                sys.exit(0)
                GPIO.cleanup()


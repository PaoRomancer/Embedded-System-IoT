import RPi.GPIO as GPIO   
import time 
channel1 = 14                       
channel2 = 15                       
channel3 = 18                       
channel4 = 17                         
channel5 = 27   
button = 12                    
GPIO.setmode(GPIO.BCM)        
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel1, GPIO.OUT)       
GPIO.setup(channel2, GPIO.OUT) 
GPIO.setup(channel3, GPIO.OUT) 
GPIO.setup(channel4, GPIO.OUT) 
GPIO.setup(channel5, GPIO.OUT) 

while 1:
      if GPIO.input (button) == 1:
            for i in range (5):
                  GPIO.output(channel5, False) 
                  GPIO.output(channel1, True)            
                  print ("LED1 on")              
                  time.sleep(0.1)              
                  GPIO.output(channel1, False)            
                  print ("LED1 off") 
                  GPIO.output(channel2, True) 
                  print ("LED2 on") 
                  time.sleep(0.1) 
                  GPIO.output(channel2, False) 
                  print ("LED2 off") 
                  GPIO.output(channel3, True) 
                  print ("LED3 on") 
                  time.sleep(0.1) 
                  GPIO.output(channel3, False) 
                  print ("LED3 off") 
            GPIO.output(channel4, True) 
            print ("LED4 on") 
            time.sleep(0.1) 
            GPIO.output(channel4, False) 
            print ("LED4 off") 
      else:
            GPIO.output(channel5, True) 
            print ("LED5 on") 
            #time.sleep(0.1) 
            #GPIO.output(channel5, False) 
            #print ("LED5 off")
             
GPIO.cleanup() 

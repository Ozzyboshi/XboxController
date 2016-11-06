import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
import XboxController




def mycallBack(controlId, value):
   if controlId == 0:
      if value > 0.5:
         print 'passo'
#         GPIO.output(23,1)
#         GPIO.output(24,0)
      elif value == 0:
          print 'passo2'
#         GPIO.output(23,0)
#         GPIO.output(24,0)
      elif value < -0.5:
          print 'passo3'
#         GPIO.output(23,0)
#         GPIO.output(24,1)
   if controlId == 12:
      if value == 1:
         print 'exiting now'
         xboxCont.stop()
         pass
   if controlId == 6:
      if value == 1:
         print 'A pressed'
         GPIO.output(4,1)
         pass
      else:
         print 'A released'
         GPIO.output(4,0) 
         pass
   if controlId == 7:
      if value == 1:
         print 'B pressed'
         GPIO.output(17,1)
         mycallBack.upPressed=1
         pass
      else:
         print 'B released'
         GPIO.output(17,0) 
         mycallBack.upPressed=0
         pass      
   if controlId == 17:
      if value[0]<=- 0.5:
         if mycallBack.leftPressed==0:
             print 'left pressed'
             mycallBack.leftPressed=1
             GPIO.output(27,1)
             pass
      elif value[0] >= 0.5:
         if mycallBack.rightPressed == 0 :
             print 'right pressed'
             mycallBack.rightPressed=1
             GPIO.output(22,1)
             pass
      else :
         if mycallBack.leftPressed==1:
             print 'Left released'
             GPIO.output(27,0)
             mycallBack.leftPressed=0
         if mycallBack.rightPressed==1:
             print 'Right released'
             GPIO.output(22,0)
             mycallBack.rightPressed=0 
         pass
      if value[1]<= -0.5:
         if mycallBack.downPressed==0:
             print 'Down pressed'
             mycallBack.downPressed=1
             GPIO.output(18,1)
             pass
      elif value[1]>= 0.5:
         if mycallBack.upPressed==0:
             print 'Up pressed'
             mycallBack.upPressed=1
             GPIO.output(17,1)
             pass
      else :
         if mycallBack.upPressed==1:
             print 'Up released'
             mycallBack.upPressed=0
             GPIO.output(17,0)
         if mycallBack.downPressed==1:
             print 'Down released'
             mycallBack.downPressed=0
             GPIO.output(18,0)
             pass

mycallBack.leftPressed=0
mycallBack.rightPressed=0
mycallBack.upPressed=0
mycallBack.downPressed=0
xboxCont = XboxController.XboxController(
   controllerCallBack = mycallBack,
   joystickNo = 0,
   deadzone = 0.5,
   scale = 1,
   invertYAxis = False)
xboxCont.start()

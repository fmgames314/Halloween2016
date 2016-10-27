from requests.auth import HTTPBasicAuth
from multiprocessing import Process
import requests
import serial
import time
import Tkinter as tk
ser = serial.Serial('COM28', 9600)

# Function definition is here
def sound_play( location, fileName ):
   "This plays a sound out of a certain speaker"
   if(location == 'front'):
       port = '6100'
   if(location == 'left'):
       port = '6101'      
   if(location == 'right'):
       port = '6102'
   if(location == 'top'):
       port = '6103'
   if(location == 'other'):
       port = '6104'
   if(location == 'main'):
      port = '6103' # just do top while you are here
      sound_play( location='left',  fileName=fileName )
      sound_play( location='right',  fileName=fileName )
   link = 'http://127.0.0.1:'+port+'/requests/status.xml?command=in_play&input=C:\halloween2016\Sound_Effects\\'+fileName
   requests.get(link, auth=HTTPBasicAuth('', 'meatball'))
   return;


# start program
sound_play( location='front', fileName='l_frontSpeaker.mp3' )
time.sleep(1)
sound_play( location='left',  fileName='l_leftSpeaker.mp3' )
time.sleep(1)
sound_play( location='right', fileName='l_rightSpeaker.mp3' )
time.sleep(1)
sound_play( location='top',   fileName='l_topSpeaker.mp3' )
time.sleep(1)
sound_play( location='other', fileName='l_otherSpeaker.mp3' )
time.sleep(1)
#raw_input("Press Enter to continue...")

while(1):

    inches = 1000;
    while(inches > 30):
       inches = ser.readline()
       inches = int(inches)
       print("inches")
       print(inches)
    ser.write('1,1,') # LightBulb On Full Power
    time.sleep(2)
    sound_play( location='left', fileName='l_creekyDoor.mp3' )
    sound_play( location='right', fileName='l_footstepsleft.mp3' )
    sound_play( location='front', fileName='l_footstepsmiddle.mp3' )
    time.sleep(3)
    sound_play( location='right', fileName='l_creekyDoor.mp3' )
    time.sleep(5)
    ser.write('1,2,') # LightBulb Flicker
    sound_play( location='top', fileName='l_MyFlickerSound.mp3' )
    time.sleep(3.5)
    ser.write('1,1,') # LightBulb On Full Power
    time.sleep(5)
    sound_play( location='main', fileName='l_ghostPass.mp3' )
    ser.write('2,1,') # LightBulb SHAKY
    time.sleep(1)
    ser.write('1,2,') # LightBulb Flicker
    time.sleep(1)
    sound_play( location='top', fileName='l_MyFlickerSound.mp3' )
    time.sleep(3.5)
    ser.write('1,0,') # LightBulb OFF This is where light bulb low power was
    sound_play( location='other', fileName='l_youWillDie.mp3' )
    time.sleep(6)
    ser.write('4,1,') # REDLED Casket lights ON
    time.sleep(2)
    ser.write('3,1,') # Casket START
    time.sleep(.5)
    sound_play( location='right', fileName='l_zomie_long.mp3' )
    time.sleep(2)
    ser.write('3,0,') # Casket END
    ser.write('4,0,') # REDLED Casket lights ON
    ser.close()
    time.sleep(200)
    
    










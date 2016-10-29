from requests.auth import HTTPBasicAuth
import Tkinter as tk
from Tkinter import *
import requests
import serial
import time
ser = serial.Serial('COM28', 9600)


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
   link = 'http://127.0.0.1:'+port+'/requests/status.xml?command=in_play&input=C:\halloween2016\CODE\Sound_Effects\\'+fileName
   requests.get(link, auth=HTTPBasicAuth('', 'meatball'))
   return;
 
class ExampleApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,master,width=300,height=200)
        # Set the title
        self.master.title('Halloween Controller')
        # This allows the size specification to take effect
        self.pack_propagate(0)
        # We'll use the flexible pack layout manager
        self.pack()
        # The go button
        self.go_button = tk.Button(self,text='Start Sequence',command=self.Start)
        self.go_button.pack(fill=tk.X, side=tk.LEFT)
        self.stop_button = tk.Button(self,text='End Sequence',command=self.Stop)
        self.stop_button.pack(fill=tk.X, side=tk.RIGHT)
        self.ser_button = tk.Button(self,text='Serial Close',command=self.SerialClose)
        self.ser_button.pack(fill=tk.X, side=tk.TOP)
        self.tarpUP_button = tk.Button(self,text='tarp UP',command=self.tarp_up)
        self.tarpUP_button.pack(fill=tk.X, side=tk.TOP)
        self.tarpDOWN_button = tk.Button(self,text='tarp DOWN',command=self.tarp_down)
        self.tarpDOWN_button.pack(fill=tk.X, side=tk.TOP)
        self.SoundTest_button = tk.Button(self,text='Sound Check',command=self.soundCheck)
        self.SoundTest_button.pack(fill=tk.X, side=tk.TOP)
        self.idle_button = tk.Button(self,text='Room Idle',command=self.idleRoom)
        self.idle_button.pack(fill=tk.X, side=tk.LEFT)
              
    def run(self):
        ''' Run the app '''
        global stage
        global lastTime
        stage = -1; lastTime = time.clock();
        while(1):
            app.update()
            if(stage == -2):
                ser.write('1,1,') # LightBulb On Full Power
                stage = -3
            ############      MAIN SEQUENCE      ############
            if(time.clock()-lastTime >  2 and stage == 0 ):
                stage+=1; lastTime = time.clock();
                ser.write('2,1,') # LightBulb SHAKY
                sound_play( location='main', fileName='l_ghostPass.mp3' ) # SOUND
            if(time.clock()-lastTime > 1.5 and stage == 1 ):
                stage+=1; lastTime = time.clock();
                ser.write('1,2,') # LightBulb Flicker
                sound_play( location='top', fileName='l_MyFlickerSound.mp3' ) # SOUND
                
            if(time.clock()-lastTime > 3.5 and stage == 2 ):
                stage+=1; lastTime = time.clock();
                ser.write('1,1,') # LightBulb On Full Power
                
            if(time.clock()-lastTime > 1 and stage == 3 ):
                stage+=1; lastTime = time.clock();
                ser.write('1,0,') # LightBulb OFF
                ser.write('7,1,') # BlackLight ON
                sound_play( location='left', fileName='l_Mcalay.wav' ) # SOUND                
                
            if(time.clock()-lastTime > 2 and stage == 4 ):
                stage+=1; lastTime = time.clock();
                ser.write('5,1,') # Creepy LEtters on, takes 10-13 seconds to complete
                
            if(time.clock()-lastTime > 16 and stage == 5 ):
                stage+=1; lastTime = time.clock();
                ser.write('4,1,') # REDLED Casket lights ON
                sound_play( location='right', fileName='l_thud.wav' ) # SOUND
                sound_play( location='front', fileName='l_thud.wav' ) # SOUND
                ser.write('7,0,') # BlackLight ON
                
            if(time.clock()-lastTime > 2 and stage == 6 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,1,') # Casket START
                sound_play( location='right', fileName='l_MixSet_A.wav' ) # SOUND
                sound_play( location='front', fileName='l_MixSet_A.wav' ) # SOUND
                
            if(time.clock()-lastTime > 1 and stage == 7 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,2,') # Casket START
                sound_play( location='right', fileName='l_zomie_long.mp3' ) # SOUND
                
            if(time.clock()-lastTime > 3 and stage == 8 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,0,') # Casket END
                ser.write('4,0,') # REDLED Casket lights OFF
                


                
            inches = ser.readline()
            inchesNUM = int(inches)
            print("inches: "+inches)
        

        
    def Start(self):
        print('start')
        global stage
        global lastTime
        stage = 0; lastTime = time.clock();
        
    def Stop(self):
        global stage
        stage = -1;
        print('stop')
        
    def SerialClose(self):
        ser.close()
        import sys
        sys.exit()
        exit();
    def tarp_up(self):
        ser.write('6,2,') # Bring Tarp UPP
    def tarp_down(self):
        ser.write('6,1,') # Bring Tarp DOWNN
    def idleRoom(self):
        global stage
        stage = -2;
    def soundCheck(self):
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



app = ExampleApp(tk.Tk())
app.run()







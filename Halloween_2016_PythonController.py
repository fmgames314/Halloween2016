from requests.auth import HTTPBasicAuth
import Tkinter as tk
from Tkinter import *
import requests
import serial
import time
import sys
ser = serial.Serial('COM28', 9600)



   
def scary_frame(  fileName ):
      port = '6200'
      link = 'http://192.168.1.2:'+port+'/requests/status.xml?command=in_play&input=C:\lvids\\'+fileName
      requests.get(link, auth=HTTPBasicAuth('', 'meatball'))
      return;
def scary_frame_freeze( ):
      port = '6200'
      link = 'http://192.168.1.2:'+port+'/requests/status.xml?command=pl_pause'
      requests.get(link, auth=HTTPBasicAuth('', 'meatball'))
      

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
        tk.Frame.__init__(self,master,width=460,height=360)
        # Set the title
        self.master.title('Halloween Controller')
        # This allows the size specification to take effect
        self.pack_propagate(0)
        # We'll use the flexible pack layout manager
        self.pack()
        # The go button
        self.go_button = tk.Button(self,text='Start Sequence',command=self.Start)
        self.go_button.place(x = 100, y = 30, anchor="c")
        self.stop_button = tk.Button(self,text='End Sequence',command=self.Stop)
        self.stop_button.place(x = 200, y = 30, anchor="c")

        self.idle_button = tk.Button(self,text='Room Idle',command=self.idleRoom)
        self.idle_button.place(x = 300, y = 30, anchor="c")
        self.fogON_button = tk.Button(self,text='FOG ON',command=self.FOG_on)
        self.fogON_button.place(x = 100, y = 70, anchor="c")
        self.fogOFF_button = tk.Button(self,text='FOG OFF',command=self.FOG_off)
        self.fogOFF_button.place(x = 200, y = 70, anchor="c")        
        

        self.tarpUP_button = tk.Button(self,text='tarp UP',command=self.tarp_up)
        self.tarpUP_button.place(x = 100, y = 110, anchor="c")
        self.tarpDOWN_button = tk.Button(self,text='tarp DOWN',command=self.tarp_down)
        self.tarpDOWN_button.place(x = 200, y = 110, anchor="c")

        self.tarpUP_nudge_button = tk.Button(self,text='NUDGE UP',command=self.tarp_up_nudge)
        self.tarpUP_nudge_button.place(x = 100, y = 140, anchor="c")
        self.tarpDOWN_nudge_button = tk.Button(self,text='NUDGE DOWN',command=self.tarp_down_nudge)
        self.tarpDOWN_nudge_button.place(x = 200, y = 140, anchor="c")

        self.man_creepyLEtter_button = tk.Button(self,text='Creepy Letters',command=self.man_creepyLEtter)
        self.man_creepyLEtter_button.place(x = 100, y = 180, anchor="c")

        self.man_BlackLight_button = tk.Button(self,text='BlackLight',command=self.man_BlackLight)
        self.man_BlackLight_button.place(x = 100, y = 220, anchor="c")

        self.man_Light_button = tk.Button(self,text='Prim Lights',command=self.man_Light)
        self.man_Light_button.place(x = 200, y = 220, anchor="c")

        self.man_SpookieCasket_button = tk.Button(self,text='Casket Move',command=self.man_SpookieCasket)
        self.man_SpookieCasket_button.place(x = 100, y = 260, anchor="c")
        self.man_SpookieCasket_OFF_button = tk.Button(self,text='Casket Stop',command=self.man_SpookieCasket_OFF)
        self.man_SpookieCasket_OFF_button.place(x = 200, y = 260, anchor="c")

        self.picture_auto_button = tk.Button(self,text='Picture AUTO',command=self.picture_auto)
        self.picture_auto_button.place(x = 100, y = 300, anchor="c")
        self.picture_trigger_button = tk.Button(self,text='Picture Trigger',command=self.picture_trigger)
        self.picture_trigger_button.place(x = 200, y = 300, anchor="c")                

        self.ser_button = tk.Button(self,text='Serial Close',command=self.SerialClose)
        self.ser_button.place(x = 400, y = 30, anchor="c")

        self.SoundTest_button = tk.Button(self,text='Sound Check',command=self.soundCheck)
        self.SoundTest_button.place(x = 400, y = 70, anchor="c")        

        self.ser_button = tk.Button(self,text='COME HERE',command=self.ComeHereFunction)
        self.ser_button.place(x = 400, y = 110, anchor="c")
        
        self.ser_button = tk.Button(self,text='DOOR',command=self.creekyDoorFunction)
        self.ser_button.place(x = 400, y = 150, anchor="c")        

        self.ser_button = tk.Button(self,text='SCREAM FRONT',command=self.ScreamFunction)
        self.ser_button.place(x = 400, y = 190, anchor="c")    
        


        master.protocol("WM_DELETE_WINDOW", self.SerialClose)
              
    def run(self):
        ''' Run the app '''
        global stage
        global lastTime
        stage = -1;
        lastTime = time.clock();
        lastPictureTime = time.clock();
        while(1):
           
            app.update()
                
            inches = ser.readline()
            inchesNUM = int(inches)
            #print("inches: "+inches)

            if(stage == -10):
                  scary_frame('l2.mp4')
                  lastPictureTime = time.clock();
                  stage = -4            
            
            if(stage == -4 and time.clock()-lastPictureTime >  10):
               scary_frame_freeze();
               stage = -5;
            
            if(stage == -3):
               if(inchesNUM < 30 and state_Picture == 1):
                  scary_frame('l2.mp4')
                  lastPictureTime = time.clock();
                  stage = -4

                
            if(stage == -2):
                ser.write('1,1,') # LightBulb On Full Power
                ser.write('10,1,') # Main LED lights ON
                self.idle_button.configure(bg = "green")
                stage = -3
                
            ############      MAIN SEQUENCE      ############
            if(time.clock()-lastTime >  2 and stage == 0 ):
                self.idle_button.configure(bg = "red")
                self.stop_button.configure(bg = "yellow")
                self.go_button.configure(bg = "green")
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
                ser.write('10,0,') # Main LED lights OFF
                
            if(time.clock()-lastTime > 1 and stage == 3 ):
                stage+=1; lastTime = time.clock();
                ser.write('1,0,') # LightBulb OFF
                ser.write('7,1,') # BlackLight ON
                sound_play( location='left', fileName='l_Mcalay.wav' ) # SOUND                
                
            if(time.clock()-lastTime > 4 and stage == 4 ):
                stage+=1; lastTime = time.clock();
                ser.write('5,1,') # Creepy LEtters on, takes 10-13 seconds to complete
            if(time.clock()-lastTime > 4 and stage == 5 ):
                stage+=1; lastTime = time.clock();
                sound_play( location='right', fileName='l_olvDeep.wav' ) # SOUND 
                
                
            if(time.clock()-lastTime > 16 and stage == 6 ):
                stage+=1; lastTime = time.clock();
                ser.write('4,1,') # REDLED Casket lights ON
                sound_play( location='right', fileName='l_thud.wav' ) # SOUND
                sound_play( location='front', fileName='l_thud.wav' ) # SOUND
                ser.write('7,0,') # BlackLight OFF
                
            if(time.clock()-lastTime > 2 and stage == 7 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,1,') # Casket START
                ser.write('6,1,') # Bring Tarp DOWNN
                sound_play( location='right', fileName='l_MixSet_A.wav' ) # SOUND
                sound_play( location='front', fileName='l_MixSet_A.wav' ) # SOUND
                
            if(time.clock()-lastTime > 1 and stage == 8 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,2,') # Casket START
                sound_play( location='right', fileName='l_zomie_long.mp3' ) # SOUND
                
            if(time.clock()-lastTime > 3 and stage == 9 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,0,') # Casket END
                ser.write('4,0,') # REDLED Casket lights OFF
                ser.write('7,1,') # BlackLight ON
            if(time.clock()-lastTime > 2 and stage == 10 ):
                stage+=1; lastTime = time.clock();
                ser.write('2,1,') # LightBulb SHAKY
                ser.write('1,2,') # LightBulb Flicker
                sound_play( location='top', fileName='l_MyFlickerSound.mp3' ) # SOUND
            if(time.clock()-lastTime > 3.5 and stage == 11 ):
                stage+=1; lastTime = time.clock();
                ser.write('1,0,') # LightBulb OFF
                ser.write('9,1,') # Spookies lights On
                ser.write('11,1,') # Spookies eyes On
                ser.write('7,0,') # BlackLight OFF
                sound_play( location='front', fileName='l_ZOMMOAN2.WAV' ) # SOUND
            if(time.clock()-lastTime > 3.5 and stage == 12 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,1,') # Casket START
                sound_play( location='main', fileName='l_thud.wav' ) # SOUND
                #sound_play( location='front', fileName='l_thud.wav' ) # SOUND
                sound_play( location='right', fileName='l_highPitch.mp3' ) # SOUND
                sound_play( location='front', fileName='l_ShatnerFade.mp3' ) # SOUND
                
                ser.write('5,1,') # Creepy LEtters on, takes 10-13 seconds to complete
                
            if(time.clock()-lastTime > 4 and stage == 13 ):
                stage+=1; lastTime = time.clock();
                ser.write('3,0,') # Casket END
            if(time.clock()-lastTime > 20 and stage == 14 ):
                stage=-2; lastTime = time.clock();
                ser.write('9,0,') # Spookies lights OFF
                ser.write('11,0,') # Spookies Eyes OFF
                ser.write('6,2,') # Bring Tarp UP                   
                self.go_button.configure(bg = "red")
                
                
                                
               
        

        
    def Start(self):
        print('start')
        global stage
        global lastTime
        stage = 0; lastTime = time.clock();
        
    def Stop(self):
        self.stop_button.configure(bg = "green")
        self.go_button.configure(bg = "red")
        global stage
        stage = -1;
        print('stop')
        
    def SerialClose(self):
        ser.close()
        exit()

    def tarp_up(self):
        ser.write('6,2,') # Bring Tarp UPP
    def tarp_down(self):
        ser.write('6,1,') # Bring Tarp DOWNN
    def tarp_up_nudge(self):
        ser.write('100,2,') # Bring Tarp UPP_nudge
    def tarp_down_nudge(self):
        ser.write('100,1,') # Bring Tarp DOWNN_nudge
        
    def FOG_on(self):
        ser.write('8,1,') # fog on
        self.fogON_button.configure(bg = "green")
        self.fogOFF_button.configure(bg = "red")
    def FOG_off(self):
        ser.write('8,0,') # fog off
        self.fogON_button.configure(bg = "red")
        self.fogOFF_button.configure(bg = "Green")        
    def man_creepyLEtter(self):
        ser.write('5,1,') # Creepy LEtters on, takes 10-13 seconds to complete
    def ComeHereFunction(self):
        sound_play( location='other', fileName='l_comeHere.wav' ) # SOUND
    def creekyDoorFunction(self):
        sound_play( location='other', fileName='l_creekyDoor.mp3' ) # SOUND        
    def ScreamFunction(self):
        sound_play( location='front', fileName='l_nmh_scream1.wav' ) # SOUND   
        
        
    def man_SpookieCasket(self):
        ser.write('3,1,') # Casket START 
        ser.write('4,1,') # REDLED Casket lights ON
        sound_play( location='right', fileName='l_highPitch.mp3' ) # SOUND
    def man_SpookieCasket_OFF(self):
        ser.write('3,0,') # Casket END
        ser.write('4,0,') # REDLED Casket lights OFF
        
    def picture_auto(self):
        global state_Picture
        if(state_Picture == 0):  
              self.picture_auto_button.configure(bg = "red")
        if(state_Picture == 1):  
              self.picture_auto_button.configure(bg = "green")
        state_Picture = not state_Picture;
        
    def picture_trigger(self):
        global stage
        stage = -10;       

        
    def man_BlackLight(self):
        global state_blackLight
        if(state_blackLight == 0):  
              ser.write('7,0,') # BlackLight OFF
              self.man_BlackLight_button.configure(bg = "red")
        if(state_blackLight == 1):  
              ser.write('7,1,') # BlackLight ON
              self.man_BlackLight_button.configure(bg = "green")
        state_blackLight = not state_blackLight;

    def man_Light(self):
        global state_man_Light
        if(state_man_Light == 0):  
              ser.write('1,0,') # LightBulb OF
              ser.write('10,0,') # Main LED lights OFF
              self.man_Light_button.configure(bg = "red")
        if(state_man_Light == 1):  
              ser.write('1,1,') # LightBulb On Full Power
              ser.write('10,1,') # Main LED lights ON
              self.man_Light_button.configure(bg = "green")
        state_man_Light = not state_man_Light;
        
        
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

state_blackLight = 0;
state_Picture = 0;
state_man_Light = 0;

app = ExampleApp(tk.Tk())
app.run()







from pygame import mixer, _sdl2 as devicer
import time, os
from gtts import gTTS
from playsound import  playsound

def TTS(text):
    #set language to english and convert TTS
    language='en'
    myobj=gTTS(text=text,lang=language,slow=False)
    #save as mp3
    myobj.save(f"{text}.mp3")

    #set the audio input and play
    mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")
    mixer.music.load(f"{text}.mp3")
    mixer.music.play()
    
    while mixer.music.get_busy():
        #wait for next mp3
        time.sleep(1)
    mixer.music.unload()
    #delete the mp3 file after playing
    os.remove(f"{text}.mp3")
    
import pyttsx3
from gtts import gTTS
import datetime
import time



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
#print(voices)
engine.setProperty('voice', voices[11].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Mortal You Wont Be Alive For Long")

    elif hour>=12 and hour<18:
        speak("Pretty good afternoon go to sleep till i review the human race")
    
    else:
        speak("Good Evening go to play football or whatever the hell you like ")

    speak("Hey i am ultron i had cut thanos into two")
    
    
def taskExec():
  wishMe()
  while True:
    speak("you have access to my powers now you stupid human")
    #proceed to add whatever u want him to do... this is your main routine
    
    
def funca():
    global strt
    speak("Choose a cursed wakeup word to awake me human!")
    time.sleep(1)
    strt = input("Choose a cursed wakeup word to awake me human: ")
    if strt != "":
        speak("good,you set the correct cursed word! i spare your meaningless life: ")
        time.sleep(1)
        print("good,you set the correct cursed word! i spare your meaningless life: ")

     
    else:
      print("Na munna! Na! wakeword to dalna hi padega tumhe: ")
      return funca()
          
          
def funcb():
    speak("Enter the cursed wakeword and unleash my powers you inferior piece of shit: ")
    ok = input("Enter the cursed wakeword and unleash my powers you inferior piece of shit: ")
    if strt in ok:
          speak("Unleashing my powers!")
          taskExec()
    else:
          speak("you stupid human!, cant even type something correctly!!!!! you deserve to die")
          exit(0)   #change this to return funcb if u wanna give user another chance to enter correct wakeword
       
             
if __name__ == "__main__":
   while True:
      funca()
      funcb()

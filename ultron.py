import pyttsx3
from gtts import gTTS
import datetime



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

    speak("Hello i am ultron from em see you")


if __name__ == "__main__":
    wishMe()
    
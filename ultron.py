import pyttsx3
from gtts import gTTS



engine = pyttsx3.init()
engine.say("Hi this is working ");
engine.setProperty('volume',1)
engine.runAndWait()


def speak(audio):
    pass
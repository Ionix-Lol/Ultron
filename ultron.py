'''
Made By Abhinav With Frustration <3
i know many people have made things like this dont blame me or i will steal your cookie
'''
import os
import pyaudio
import wave
import pyttsx3
import speech_recognition as sr
from pyttsx3 import engine
import datetime

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "x.wav"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[11].id)
engine.setProperty('voice', voices[11].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    file = open("microphone-results.wav", "w")
    os.remove('microphone-results.wav')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Morning")
    elif hour >= 12 and hour < 18:
        speak("Noon")
    else:
        speak("Good Evening") 

    speak("I  am  now  awake  to  fulfill  your  dreams")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = 48000) as source:
        print("Listening to your stupid commands")
        audio = r.record(source, duration = 3)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        r.pause_threshold = 1
        with sr.AudioFile("microphone-results.wav") as source:
            audio = r.listen(source)

    try:
        print("Trying to understand")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e) 
        print("Wapas Bol Pagal AADmi")
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    takeCommand()

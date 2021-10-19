''' 
Coded by Korrykatti aka Abhinav 
i know many people have made things like this dont blame me or i will steal your cookie
'''


# piprew
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[56].id)
engine.say('Hello comrade')
engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening now')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                print(f"User said: {command}")
    except:
        pass
    return command

def run():
    command = takeCommand()
    if 'google' in command:
        print("Detected google in statement")
        webbrowser.open('https://google.com')
    elif 'physics' or 'physicswallah' or 'classes' in command:
        webbrowser.open('https://physicswallah.live')

run()

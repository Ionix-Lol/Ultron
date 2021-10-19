''' 
Coded by Korrykatti aka Abhinav 
'''



import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices =engine.getProperty('')
try:
    with sr.Microphone() as source:
        print('listening now')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'ultron' in command:
            print(command)
except:
    pass
import speech_recognition as sr

listener = sr.Recognizer()
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
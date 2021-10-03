#Note: Limited to Windows users
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)   #just to check which voices available on your system :D
engine.setProperty('voice', voices[1].id)  #male voice like jarvis :( couldnt get ultron wala with this engine on the internet, the recognition sucks anyways
# engine.setProperty('rate', 195) 

#make functions and enjoy life
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning master ")

    elif hour>=12 and hour<16:
        speak("Good Afternoon master ")   

    else:
        speak("Good Evening master ")  

    
def takeCommand():   
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        #playsound("C:\\Users\\Admin\\Desktop\\AVA\\ping.mp3")  #added this to troubleshoot the SR issues
        print("Listening...") #you can alter with the below settings as per you need
        # r.energy_threshold = 50
        # r.dynamic_energy_threshold = True
        r.pause_threshold = 0.5
        # r.adjust_for_ambient_noise(source, duration=0.5)
        # r.non_speaking_duration = 1
        # r.operation_timeout = None   #to be used when playing with API integration 
        audio = r.listen(source)
        # audio = r.listen(source, phrase_time_limit=0.5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        #integer = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        # print(f"   said: {integer}\n")

    except Exception as e:
        #print(e)   
          #speak("Could you please repeat that master?") 
          print("Could you please repeat that ?")  
          return "None"
    return query 
  
if __name__ == "__main__":   
    
    def taskExecution(): 
       while True:
        query = takeCommand().lower() 
        # schedule.running_pending()
        if 'hi' in query:
          speak("hi, I am Ultron")  
                
        elif 'who created you' in query:
                speak("Master Abhinav created my existence and i am grateful for this")
                
        elif 'what is your purpose' in query:
                speak("The only purpose of my existence is to slay and conquer inferior human life form")


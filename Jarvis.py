import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning!")
        
    elif hour >=12  and hour < 18:
        speak("Good Afternoon!")        
        
    else:
        speak("Good Evening!")    
        
    speak("I am jarvis, your AI assistant sir, How may i help you? ")    


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query   
    
if __name__ == "__main__":
    wishMe()
    while True:   #we can use while True: for continuos listening.
        query = takeCommand().lower()
        
        
          # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 4)
            print("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")    
            
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'E:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            
            
        elif 'open visual code' in query:
            codePath = "E:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            
         # We can apply this method for any app present in our system.
        
         
            
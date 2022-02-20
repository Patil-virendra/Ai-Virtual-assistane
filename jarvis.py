import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser 
import os  
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi This is Jarvis. Please tell me how can I help you sir")  

def takeCommand():
    # it take microphone input from the user and returns string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-IN')
        print("User said:", query)

    except Exception as e:
        print(e)
        print("say that again please......" )
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('virendrapatil1012@gmail.com','8999471192Vsp*')
    server.sendmail('virendrapatil1012@gmail.com', to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
 
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'open youtube' in query:    
            webbrowser.open("youtube.com")
        elif'open google' in query:    
            webbrowser.open("google.com")
        elif'open instagram' in query:    
            webbrowser.open("instagram.com")
        elif'open stackoverflow' in query:    
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'F:\Rock'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"sir, the time is {strfTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Virendra Patil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)

        elif 'email to virendra' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "virendrapatil1012@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry mail not send")
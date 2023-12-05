import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buenas Dias!")

    elif hour>=12 and hour<18:
        speak("Oh kaka, Good Afternoon!")   

    elif hour>=18 and hour<21:
        speak("Good Evening!")

    else:
                 speak("Oh Big boy you should probably sleep now. Buenas noches")



    speak("I'm Kishor dada, Amigo. Just say, how may I be helpful to ya")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('plaspvamids6628951@gmail.com', 'Jacobssipybby+//9780#@mattersz')
    server.sendmail('plaspvamids6628951l@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open NETFLIX' in query:
            webbrowser.open("www.netflix.com/browse")   

        elif 'open Spotify' in query:
            webbrowser.open("spotify.com")

        
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"ok chum, it is {strTime}")




        elif 'your name' in query:
            speak("Okay man, you dunno my name! It is SSIPY. and please do not ask me what it stands for? alright chum?")


        elif 'stands for' in query:
            speak("Ooh man, I told ya not to ask! are ya crazy dude?")   



        elif 'play a movie' in query:
            ooppss = ''
            print("Just select yourself") 
            speak("just pick it yourself dude!")   
            os.startfile(ooppss)


        elif 'abuse him' in query:
            speak("you are a crazy dude man! you should shut your ass up and don not fuck with me again! ok?")



        elif 'what can you do' in query:
            speak("I can play a song for you or a movie/show and I can also connect you to browser or send a mail.. else a netflix/spotify time you know it dude!!")

            print("play a song, movie/show, browser, send a mail, netflix/spotify, time you know it dude!!")







        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email to patel' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "patelvraj2529@gmail.com"    
                sendEmail(to, content)
                speak("Yep!, Email has been sent!")
            except Exception as e:
                print(e)
                speak("Lo siento chum. I am unable to send this email, try to understand!")    

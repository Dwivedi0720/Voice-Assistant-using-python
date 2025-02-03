import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes 
import os 
import time 

def sptext(): 
    recognizer=sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source) 
        try: 
            print("recognizing...") 
            data = recognizer.recognize_google(audio)
            print(data) 
            return data
        except sr.UnknownValueError: 
            print(" Not Understand ") 

def speechtx(x):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150) 
    engine.say(x)
    engine.runAndWait ()

    if __name__ == '__main__':
 
        if  "hey peter" in sptext().lower():
            while True:

                datal=sptext().lower()

                if "your name" in data1:
                    name="my name is peter"
                    sppechtx(name)

                elif"old are you" in data1:
                    age="i am two years old"
                    speechtx(age)

                elif 'time' in data1:
                    time=datatime.datatime.now().strftime("%I%M%P")
                    speechtx(time)

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")


                elif 'web'in data1:
                    webbrowser.open("")

                elif "joke" in data1:
                    joke_1=pyjokes.get_jokes(language="en",category="neytral")
                    print(joke_1)
                    speechtx(joke_1)

                elif 'play song' in data1:
                    add=""
                    listening=os.listdir(add)
                    print(listsongs)
                    os.startfile(os.path.join(add,listsong[1]))

                elif "exit" in data1:
                    speechtx("thank you")
                    break
                    
            time.sleep(10)
    else:
        print("thanks")
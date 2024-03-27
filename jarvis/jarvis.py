'''
Author: kral hacker
Date: 4/01/2023
Purpose: To make a basic voice assistant named jarvis
'''


import pyttsx3
import speech_recognition as sr

Assistant= pyttsx3.init('sapi5')
voices= Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()

def takecommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        command.pause_threshold=1
        audio=command.listen(source)

        try:
            print("Recognizing.....")
            query =command.recognize_google(audio,language='en-in')
            print(f"You Said: {query} ")

        except Exception as Error:
            return "none"
        return query.lower()

def TaskExe():
    while True:
        query= takecommand()
        if "hello" in query:
            Speak("hello sir, i am jarvis")
            Speak("your personal Ai assistant, how may i help you")

        elif "how are you" in query:
            Speak("am good sir, how about you")

        elif "go to sleep" in query:
            Speak("ok sir, you can call me anytime")
            break
        elif "kya hal hai" in query:
            Speak("mai badiya, aap sunao")

        elif "bye" in query:
            Speak("Okay sir ")
            Speak("bye")
            break
        elif "main Achcha hoon" in query:


            Speak("main bhi")

TaskExe()
# -*- coding: utf-8 -*-
"""
@author Vindhyaa Saravanan
"""


# Importing modules required
import pyttsx3
import speech_recognition as recog
import datetime
import wikipedia
import webbrowser
import os

#  Setting up speech settings
engine = pyttsx3.init('sapi5')

# Set Rate of Speech
engine.setProperty('rate', 170)

# Set Volume of Speech
engine.setProperty('volume', 2.0)

# Seting a Female voice for the ChatBot
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# FUNCTION TO SPEAK GIVEN AUDIO
"""
Function to speak a given piece of audio.
"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# FUNCTION TO TAKE AND INTERPRET COMMAND
"""
Function to listen to user's spoken command, 
and interpret it into a string.
"""
def takeCommand():
    # Request command by speaking
    speak("What would you like me to do for you?")
    
    # Listen, record user's command and interpret
    r = recog.Recognizer()
    with recog.Microphone() as audio_source:
        print("Listening...")
        r.pause_threshold = 1
        # Save user's audio command
        audio = r.listen(audio_source)

        # Recognize command (audio to text) using Google
        try:
            print("Recognizing...")
            # Recognize and print the command
            request = r.recognize_google(audio, language='en-in')
            print(f"User said: {request}")

        # If not recognized
        except Exception:
            # Print error message
            print("Sorry, I couldn't quite catch that.")
            # No interpreted output to return
            return "None"

    # Return interpreted command
    return request


# FUNCTION TO WISH USER
def wishMe():
    # Greet as per time of day
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    # Greet the user
    speak("Hello, User!")


#----------------------------- MAIN FUNCTION ---------------------------------
if __name__=="__main__" :

    # Greet the user
    username = "Vindhyaa"
    wishMe()

    # Take first command
    request = takeCommand().lower()

    # Run command through E.D.I.T.H list of functions and implement functions

    # Reprompting if command isn't understood
    if request == "None":
        speak("Could you please repeat what you just said?")
        request = takeCommand().lower()

    # Telling user the time
    if "the time" in request:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{username}, the time is {strTime}")

    # Running a Wikipedia search
    elif 'wikipedia' in request:
        speak('Searching Wikipedia...')
        request = request.replace("wikipedia", "")
        results = wikipedia.summary(request, sentences = 2)
        speak("According to Wikipedia")
        print("According to Wikipedia:")
        print(results)
        speak(results)

    # Opening Youtube
    elif 'youtube' in request:
        webbrowser.open("youtube.com")

    # Opening Google
    elif 'google' in request:
        webbrowser.open("google.com")

    # Opening Minerva
    elif 'minerva' in request:
        webbrowser.open("minerva.leeds.ac.uk")

    # Playing music
    elif 'play music' in request:
            music_dir = 'C:\\Users\\vindh\\Desktop\\Music\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
           
    # If request is not in list of functions
    else:
        speak("Sorry, I can't help you with this.")
        speak("Is there anything else I can do for you?")
        
        # Quit the program if user done with chatbot
        answer = takeCommand().lower()
        if 'no' in answer:
            exit
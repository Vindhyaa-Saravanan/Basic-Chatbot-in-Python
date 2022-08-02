# Basic-Chatbot-in-Python

Experimentation with creating a very basic chatbot, to
function as a personal assistant for my needs.

Functions:
    Wish the user upon being run
    Interpret spoken commands
    Tell the time
    Search wikipedia for a particular topic
    Open Youtube, Google etc
    Play music from a directory on the same device
    
# Prerequisites

The following modules have been used in this program:
## pyttsx3
pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with Python 2 and 3.
## SpeechRecognition
This allows us to convert audio into text for further processing.
## datetime
The datetime module supplies classes for manipulating dates and times.
## wikipedia
Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
## webbrowser
The webbrowser module provides a high-level interface to allow displaying web-based documents to users. Under most circumstances, simply calling the open() function from this module will do the right thing.
## os
The OS module in Python provides functions for interacting with the operating system and comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. 

Install the above modules by entering into the terminal:
'''{r}
pip install pyttsx3
pip install SpeechRecognition
pip install datetime
pip install wikipedia
pip install webbrowser
pip install os
pip install PyAudio
'''

# Running the Program
to run this program, enter into terminal:
'''{r}
python chatbot.py
'''

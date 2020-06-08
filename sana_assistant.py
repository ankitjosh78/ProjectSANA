import datetime
import os
import random
import re
import time
import urllib.parse
import urllib.request

import speech_recognition as sr
import wikipedia
from gtts import gTTS
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# the speak function takes input as a text. When we will give input as voice we have to use sr and convert it to text.
def speak(audio):
    print(audio)  # It prints whatever it is going to say.

    file = "SANA_reply_" + str(time.time()) + '.mp3'

    text_to_speech = gTTS(text=audio, lang='en-uk', slow=False)  # This converts our text to speech.

    text_to_speech.save(file)

    playsound(file)  # It plays sound

    os.remove(file)  # It deletes the file after its use


# greets the user depending upon the time of the day
def greet_user():
    current_hour = int(datetime.datetime.now().hour)

    if 0 <= current_hour < 4:
        speak("Why are you still awake ? You night owl !")

    elif 4 <= current_hour < 12:
        speak("Good Morning ")

    elif 12 <= current_hour < 16:
        speak("Good Afternoon")

    elif 16 <= current_hour <= 22:
        speak("Good Evening ")

    else:
        speak("Good Night .")

    speak("Hi sir, I'm Sana, what can I do for you ?")


# The listen function listens our voice ,recognizes it and tries to translate it to a string

def listen():
    listener = sr.Recognizer()  # I am initializing the listener

    with sr.Microphone() as source:
        print("SANA is ready...")

        listener.pause_threshold = 1  # wait for 1 seconds for the voice

        listener.adjust_for_ambient_noise(source, duration=1)  # so that the noise is less

        audio = listener.listen(source)  # listens

    try:  # tries to translate it
        print("Recognizing.....")

        command = listener.recognize_google(audio, language='en-in').lower()  # lower() so that there is no case issues

        print("You said :", command + '\n')

    except sr.UnknownValueError:  # if due to some reason it could not hear us
        speak("Your last command couldn\'t be heard")

        command = listen()  # infinite loop and tries to listen to us again

    return command  # returns the the command given by us as a string.


# From this part, out assistant , starts its real functioning.

# BY THE WAY, I SPENT MY 4 ENTIRE DAYS ON THIS PROJECT. DO TELL ME IF YOU LIKED IT.


def sana(command):
    if "hey what's up" in command:
        speak("Just chilling around, what can I help you with ?")

    elif "how are you" in command:
        speak("I'm good ,what about you?")

    elif "i am great" in command or "i am good" in command:
        speak("Good to hear that.")

    elif "hey sana" in command or "hello" in command:
        speak("Hey , what can I do for you?")

    elif "nothing" in command:
        speak("Alright, if you want to quit, just say stop.")

    elif "thank you" in command or "thanks" in command:
        speak("You are welcome ")

    elif "nice" in command or "cool" in command or "awesome" in command or "great" in command:
        speak("I'm glad, you liked it.")

    elif "who made you" in command or "who developed you" in command:
        speak("I was made by Ankit Josh and am being continuosly developed more.")

    # This where the chatting part ends. From now there will just be different functionalities

    
    elif "time" in command:  # tells the time using datetime module
        str_time = datetime.datetime.now().strftime("%H:%M:%S")

        speak(f"The time is {str_time}")

    elif 'open google and search' in command:  # to make a google search, example:open google and search coronavirus.
        reg_ex = re.search('open google and search (.*)', command)

        if reg_ex:
            search_for = command.split("search", 1)[1]

            speak('Opening Google.....')

            driver = webdriver.Chrome()

            driver.get('http://www.google.com')

            search = driver.find_element_by_name('q')

            search.send_keys(str(search_for))

            search.send_keys(Keys.RETURN)

    elif 'github' in command:  # opens your github account.

        driver = webdriver.Chrome()

        driver.get('http://www.github.com/ankitjosh78')  # use your own account id here.

    elif 'youtube' in command:  # to play a video on youtube. example:open youtube play carryminati. It goes with the
        # first search result.

        speak('Opening Youtube.....')

        reg_ex = re.search('youtube (.+)', command)  # similar to open google

        if reg_ex:
            domain = command.split("youtube", 1)[1]

            query_string = urllib.parse.urlencode({"search_query": domain})

            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)

            search_results = re.findall(r'href=\"/watch\?v=(.{11})', html_content.read().decode())

            s = ("http://www.youtube.com/watch?v={}".format(search_results[0]))

            driver = webdriver.Chrome()

            driver.get(s)
    
    
    elif "wikipedia" in command:  # example: cristiano ronaldo wikipedia
        speak("Searching Wikipedia....")

        command = command.replace("wikipedia", "")

        results = wikipedia.summary(command, sentences=2)

        speak("According to Wikipedia")

        speak(results)
    
    
    elif 'play music' in command:  # to play a random song from a local directory using groove
        music_location = 'F:\\Songs'  # the directory from which you want to play the songs
        song_names = os.listdir(music_location)
        n = random.randint(0,
                           99)  # generates a random number between 0 to 99. 99 because I have 100 songs only in that
        # dir.

        os.startfile(os.path.join(music_location, song_names[n]))

    elif "stop" in command or "quit" in command or "bye" in command:
        speak("Okay,see you later :)")

        quit()  # quits the entire program.


# I'm leaving spaces for more functions that I might add later.


if __name__ == "__main__":  # the main function , it is optional though
    greet_user()  # wishes the user

    while True:  # infinite loop to continue conversations.

        sana(listen())  # this function returns the string of our voice from the listen function to the sana function.

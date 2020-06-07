#Required libraries and modules. 
# The assistant will be able to do what we say.
#example: If we say open google and search something, it should search for something
#If we ask hey sana what is the time? It will tell the time
#If we ask play music for me then it will play music from a specific directory.
#If we ask for information about someone(celeb) it will fetch that from wikipedia.
#It can send e-mail via smtp module of python
#It should be even able to search for a specific title said by us in youtube
#I am going to write beside all the libraries its purpose.
#I will suggest you to use VS code.


#FINALLY, I have put in a lot of effort into this so take your time in reading the instructions and the comments.
#I can assure you ,you will definitenely learn /understand.


import speech_recognition as sr #for speech recognition ,in the project we will call it sr
from gtts import gTTS #for text to speech conversion using google's api
from playsound import playsound #to play sound
import re #support for regular expression
import os #to get access to the system like opening a .mp3 file
import time #self explanatory
import datetime #self explanatory
import wikipedia #wikipedia module to get data
import random #maybe of some use somewhere
import smtplib #for sending email
from selenium import webdriver #an advanced type of web browser using tool
from selenium.webdriver.common.keys import Keys #for using selenium install the driver for your browser.I will be using chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # A web scraper , useful for getting data from websites
import requests #Useful for getting data in websites. We will see what to use and when
import urllib.request #useful to open links
import urllib.parse #nothing special just parses data.
import pyaudio #a required module to use sr

#Don't worry if you are not sure which modules to download and which not as some are inbuilt modules.
#I'm compiling the modules that you need to download and their install commands.

#speech_recognition: pip install SpeechRecognition
#gtts: pip install gTTS
#playsound :pip install playsound
#wikipedia: pip install wikipedia
#smtplib: pip install smtplib
#selenium: pip install selenium
#bs4: pip install bs4
#requests: pip install requests
#pyaudio: pip install pyaudio


#Rest of the packages are inbuilt with python

#Alright I think we are good to go.

#Let us start discussing how the assistant will work. My idea is to use sr to get the voice as a text.

#Accordingly we can perform various operation. Example: if we find the word "time" we can reply with the current time.

#the speak function takes input as a text. When we will give input as voice we have to use sr and convert it to text.

def speak(audio):
    print(audio) #So that we know it is saying
    r1=random.randint(1, 10000000) #If you are shocked why I used random module it is because if I use the speak once
    r2=random.randint(1, 10000000) #then the next time the file was getting mixed and there was an error. I do not know the probability of getting the same file though ^_^.

    
    file=str(r1)+"hahahaha"+str(r2)+'.mp3' 

    text_to_speech=gTTS(text=audio, lang='en-us', slow=False) #This converts our text to speech. I like en-us more than en-in.
    text_to_speech.save(file)                               #This saves the speech in a random named file
    
    playsound(file) #It plays sound
    
    os.remove(file) #It deletes the file after its use

# This is just a sample.




#I made this function wish_user() so that it will wish the user whenever the user runs the program.
#Depending upon the time of the day.
def greet_user():
    current_hour=int(datetime.datetime.now().hour)

    if current_hour >=0 and current_hour <4:

        speak("Why are you still awake ? You night owl !")

    elif current_hour>=4 and current_hour<12:

        speak("Good Morning " )

    elif current_hour>=12 and current_hour<16:

        speak("Good Afternoon" )

    elif current_hour>=16 and current_hour<=22:

        speak("Good Evening ")

    else:
        speak("Good Night .")

    
    speak("Hi sir, I'm Sana, what can I do for you ?")
    
    
    

#This function listens to our command. Read the documentation for sr module and some articles explaining how the module works.

def listen(): 
    listener=sr.Recognizer() #I am initializing the listener
    with sr.Microphone() as source: 
        print("SANA is ready...")
        listener.pause_threshold=1 #wait for 2 seconds for the voice

        listener.adjust_for_ambient_noise(source, duration=1) # so that the noise is less

        audio = listener.listen(source) #listens 

    try: #tries to translate it
        print("Recognizing.....")
        
        command=listener.recognize_google(audio, language='en-in').lower() #i am using lower() so that no case error is received when comparing the strings
        
        print("You said :", command+'\n') 
    
    except sr.UnknownValueError: #if due to some reason it could not hear us
        
        print("Your last command couldn\'t be heard")
        
        command=listen() #infinite loop and tries to listen to us again
    
    
    #return the the command given by us as a string.
    return command 



#From this function our assistant starts it real functioning.
#The commands are pretty much self explanatory.

#BY THE WAY, I SPENT MY 4 ENTIRE DAYS ON THIS PROJECT. DO TELL ME IF YOU LIKED IT.




#I will be adding more functionalities to it after I'm done testing them on my machine.

def sana(command): 
    
    if "hey what's up" in command:
        speak("Just chiling around, what can I help you with ?")

    elif "how are you" in command:
        speak("I'm good ,what about you?")

    elif "i am great"in command or "i am good" in command:
        speak("Good to hear that.") 

    elif "hey sana" in command or "hello" in command:
        speak("Hey , what can I do for you?")
    
    elif "nothing" in command:
        speak("Alright, if you want to quit, just say stop.")
    
    elif "thank you" in command or "thanks" in command :
        speak("You are welcome ")
    
    elif "nice" in command or "cool" in command or "awesome" in command or "great" in command:
        speak("I'm glad, you liked it.")
    
    elif "who made you" in command or "who developed you" in command:
        speak ("I was made by Ankit Josh and am being continuosly developed more.")
    
    elif "wikipedia" in command: #example: cristiano ronaldo wikipedia
        speak("Searching Wikipedia....")
        command= command.replace("wikipedia","")
        results=wikipedia.summary(command, sentences=2) #you can configure how many sentences you want to listen.
        speak("According to Wikipedia")
        speak(results)
    
    elif "time" in command:
        str_time=datetime.datetime.now().strftime("%H:%M:%S") #tells the time using datetime module
        speak(f"The time is {str_time}")
    
    
    elif 'open google and search' in command: #to make a google search. example:open google and search coronavirus.
        reg_ex = re.search('open google and search (.*)', command)  #returns to us a match object . refer to https://www.w3schools.com/python/python_regex.asp for more information
        
        if reg_ex: #ensures we have a word after the 'search'
            search_for = command.split("search",1)[1] #gets us the word(s) after the phrase 
            
            speak('Opening Google.....')
            
            driver = webdriver.Chrome() #refer to selenium module documentation for better understanding
            driver.get('http://www.google.com')
            search = driver.find_element_by_name('q')
            search.send_keys(str(search_for))
            search.send_keys(Keys.RETURN)



    elif 'youtube' in command:  #to play a video on youtube. example:youtube carryminati
        speak('Opening Youtube.....')

        reg_ex = re.search('youtube (.+)', command) #similar to open google

        if reg_ex:
            domain = command.split("youtube",1)[1] 
            query_string = urllib.parse.urlencode({"search_query" : domain}) #encodes our query with the "search query" string since youtube works like that.
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) #basically just does a search on youtube
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) #decodes the received url and stores it as a html type object
            s=("http://www.youtube.com/watch?v={}".format(search_results[0])) #goes with the first search result 
            driver = webdriver.Chrome()
            driver.get(s)
        #here it goes with the first search result since it is mostly the relevant one ,thus, the output might vary sometimes.
    
    
    
    elif 'play music' in command : #to play a random song from a local directory using groove
        music_location='F:\\Songs' #the directory from which you want to play the songs
        song_names=os.listdir(music_location) #lists all the songs and returns them in a list
        
        n=random.randint(0, 99) #generates a random number between 0 to 99. 99 because I have 100 songs only in that dir.
        
        
        os.startfile(os.path.join(music_location,song_names[n])) #starts playing a random song


    
    elif "stop" in command or "quit" in command or "bye" in command:
        speak("Okay,see you later :)")
        
        quit() #quits the entire program. 
    












#I'm leaving spaces for more functionalities that I might add later.


if __name__ == "__main__": #the main fucnction , it is optional though
    
    greet_user() #wishes the user
    
    while True: #infinite loop to continue conversations.
        
        sana(listen()) #this function returns the string of our voice from the listen function to the sana function.

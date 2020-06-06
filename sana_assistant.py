#Required libraries and modules. Probably not all will be used. But download them all (just incase)
#I think we can first make it as an assitant rather than a chat bot.
# The assistant will be able to do what we say.
#example: If we say open youtube , it will open www.youtube.com on browser
#If we ask hey sana what is the time? It will tell the time
#If we ask play some music for me then it will play music from a specific directory.
#If we ask for information about someone(celeb) it will fetch that from wikipedia.
#It can send e-mail via smtp module of python
#It should be even able to search for a specific title said by us in youtube( i am not sure how we can do this but lets see.)
# I am going to write beside all the libraries its purpose.
#I will suggest you to use VS code.




import speech_recognition as sr #for speech recognition ,in the project we will call it sr
from gtts import gTTS #for text to speech conversion using google's api
from playsound import playsound #to play sound
import pyttsx3 # it is also a tts library. works offline.
import webbrowser #speaks for itself
import re #support for regular expression
import os #to get access to the system like opening a .mp3 file
import time 
import datetime
import nltk #a natural language toolkit. may or may not be of use
import wikipedia #wikipedia module to get data
import random #maybe of some use somewhere
import smtplib #for sending email
from selenium import webdriver #an advanced type of web browser using tool
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # A web scraper , useful for getting data in websites
import requests #Useful for getting data in websites. We will see what to use and when
import urllib.request #useful to open links
import urllib.parse #nothing special just parses data.
import pyaudio #a required module to use sr

#Don't worry if you are not sure which modules to download and which not as some are inbuilt modules.
#I'm compiling the modules that you need to download and their install commands.

#speech_recognition: pip install SpeechRecognition
#gtts: pip install gTTS
#playsound :pip install playsound
#pyttsx3: pip install pyttsx3
#nltk: pip install nltk
#wikipedia: pip install wikipedia
#smtplib: pip install smtplib
#selenium: pip install selenium
#bs4: pip install bs4
#requests: pip install requests
#pyaudio: pip install pyaudio


#Rest of the packages are inbuilt with python

#Alright I think we are good to go. I want to tell you that we might not require all libraries.
#But I know about some of these libraries and know just basic about the others.Anyways it might be of use.
#Let us start discussing how the assistant will work. My idea is to use sr to get the voice as a text.
#Accordingly we can perform various operation. Example: if we find the word "time" we can reply with the current time.

#the speak function takes input as a text. When we will give input as voice we have to use sr and convert it to text.
def speak(audio):
    print(audio) #So that we know it is saying
    r1=random.randint(1,10000000) #If you are shocked why I used random module it is because if I use the speak once
    r2=random.randint(1,10000000) #then the next time the file was getting mixed and there was an error. I do not know the probability of getting the same file though ^_^.

    
    file=str(r1)+"hahahaha"+str(r2)+'.mp3' 

    text_to_speech=gTTS(text=audio,lang='en-us',slow=False) #This converts our text to speech. I like en-us more than en-in.
    text_to_speech.save(file)                               #This saves the speech in a random named file
    
    playsound(file) #It plays sound
    
    os.remove(file) #It deletes the file after its use

# This is just a sample.
#I think Sana is more easily understandable in english compared to Megha.



#I made this function wish_user() so that it will wish the user whenever the user runs the program.
#Depending upon the time of the day.
def wish_user():
    current_hour=int(datetime.datetime.now().hour)

    if current_hour >=0 and current_hour <4:

        speak("Why are you still awake ? You night owl !")

    elif current_hour>4 and current_hour<12:

        speak("Good Morning " )

    elif current_hour>12 and current_hour<16:

        speak("Good Afternoon" )

    elif current_hour>16 and current_hour<22:

        speak("Good Evening ")

    else:
        speak("Good Night .")

    
    speak("Hi sir, I'm Sana, what can I do for you ?")
    
    
    

#This function listens to our command. Read the documentation for sr module and some articles explaining how the module works.

def listen(): 
    listener=sr.Recognizer() #I am initializing the listener
    with sr.Microphone() as source: 
        print("SANA is ready...")
        listener.pause_threshold=2 #wait for 2 seconds for the voice

        listener.adjust_for_ambient_noise(source,duration=1) # so that the noise is less

        audio = listener.listen(source) #listens 

    try: #tries to translate it
        print("Recognizing.....")
        
        command=listener.recognize_google(audio,language='en-in').lower() #i am using lower() so that no case error is received when comparing the strings
        
        print("You said :",command+'\n') 
    
    except sr.UnknownValueError: #if due to some reason it could not hear us
        
        speak("Your last command couldn\'t be heard")
        
        command=listen() #infinite loop and tries to listen to us again
    
    
    #return the the command given by us as a string.
    return command 



#From this function our assistant starts it real functioning.
#The commands are pretty much self explanatory.

#BY THE WAY, I SPENT MY ENTIRE DAY ON THIS PROJECT. DO TELL ME IF YOU LIKED IT.


# I used my mobile as a wireless mic with help of an app.

#I will be adding more functionalities to it after I'm done testing them on my machine.

def sana(command): 
    
    if "hey what's up" in command:
        speak("Just chiling around, what can I help you with ?")

    elif "hey sana" in command or "hello" in command:
        speak("Hey , what can I do for you?")
    
    elif "nothing" in command:
        speak("Alright, if you want to quit, just say stop.")
    
    elif "thank you" in command or "thanks" in command :
        speak("You are welcome ")
    
    elif "nice" in command or "cool" in command or "awesome" in command or "great" in command:
        speak("I'm glad you liked it")
    
    elif "wikipedia" in command: #example: cristiano ronaldo wikipedia
        speak("Searching Wikipedia....")
        command= command.replace("wikipedia","")
        results=wikipedia.summary(command,sentences=1) #you can configure how many sentences you want to listen.
        speak("According to Wikipedia")
        speak(results)
    
    elif "time" in command:
        str_time=datetime.datetime.now().strftime("%H:%M:%S") #tells the time using datetime module
        speak(f"The time is {str_time}")
    
    
    elif 'open google and search' in command: #to make a google search. example:open google and search coronavirus.
        reg_ex = re.search('open google and search (.*)', command) 
        search_for = command.split("search",1)[1] 
        print(search_for)
        url = 'https://www.google.com/'
        
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subgoogle
        
        speak('Opening Google.....')
        driver = webdriver.Chrome()
        driver.get('http://www.google.com')
        search = driver.find_element_by_name('q')
        search.send_keys(str(search_for))
        search.send_keys(Keys.RETURN)



    elif 'youtube' in command:  #to play a video on youtube.
        speak('Opening Youtube.....')

        reg_ex = re.search('youtube (.+)', command)

        if reg_ex:
            domain = command.split("youtube",1)[1] 
            query_string = urllib.parse.urlencode({"search_query" : domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
    
    
    elif "stop" in command or "quit" in command or "bye" in command:
        speak("Okay,see you later :)")
        quit() #quits the entire program. 
    
















#I'm leaving spaces for more functionalities that I might add later.

if __name__ == "__main__": #the main fucnction , it is optional though
    
    wish_user() #wishes the user
    
    while True: #infinite loop to continue conersations.
        
        sana(listen()) #this function returns the string of our voice to the listen function.

    
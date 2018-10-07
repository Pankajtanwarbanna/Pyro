# Author - Pankaj Tanwar
# Personal virtual assistant - pyro

#========================import libraries====================================================
import speech_recognition as sr
import pyttsx3
import pyaudio
import sys
import time
import os
import winshell
import ctypes
import pyautogui
import webbrowser
import random
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
#=====================time function===============================================================
localtime = time.asctime(time.localtime(time.time()))
#=======================initilize pyttsx ====================================================
engine = pyttsx3.init()
#==================================function difined===========================================
def speak(text):
        engine.say(text);
        print(text)
        engine.runAndWait()        

def start():
        speak("Good to see you sir")
        speak("Starting all applications")
        speak("Installing all drivers")
        speak("system has been started.")
        speak("Now your bro online sir.")
        speak("How can i help you?")

def song():
        speak("I am going to play a good hindi song for you. I hope you like it.")
        a = os.listdir("F:\\Favourites\\")
        path = "F:\\Favourites\\"+random.choice(a)
        os.startfile(path)

def open_google(a):
        url = "https://www.google.co.in/search?q=" +a+ "&oq="+a+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
        webbrowser.open_new(url)        
def empty():
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
#=============================== main function (Body) =====================================
def mainfunction():
        os.system('CLS')
        print("say something..")
        a = r.listen(source)
        try:
                print("Analysing it........")
                user = r.recognize_google(a)
                print("Got it.")
                print(user)
#================================== Say hii to pyro ==============================================================
                if user == "hey pyro" or user == "hi pyro" or user == "hey Pyro" or user=="hello pyro":
                        speak("Hello pankaj, always here for your service how can i help you?")
#============================== Start system ========================================================================
                if user == "start":
                        start()
#========================================= Who is pyro ===================================================
                if user == "who are you" or user =="your name please" or user=="what's your name" or user=="your name" or user=="what is your name":
                        p =["I thought you'd never ask, so i've never thought about it.", "is that a tricky question?"]
                        speak(random.choice(p))
#======================================== How are you pyro =========================================================
                if user == "how are you":
                        speak("Quite well ,Thanks for asking")
#=============================== Close Program ======================================================================
                if  user == "shutdown" or user == "thank you" or user=="close" or user=="exit" or user=="Exit":
                        speak("It was a great time with you pankaj, Thank you.")
                        sys.exit()
#================================ What can Pyro do ===============================================================
                if user == "what can you do":
                        speak("It's all depends on my code!")
#======================================= Who is your owner ===========================================================
                if user== "what is your owner name" or user=="your owner name":
                        speak("My owner name is Pankaj Tanwar")
#====================================== Asking Time ====================================================================
                if user == "what time is it" or user == "can you tell me the time" or user== "can you tell me time":
                        speak(localtime)
#======================================= Who is Pankaj ==================================================================
                if user == "who is pankaj" or user == "who is Pankaj":
                        speak("Pankaj is my owner , He is a good guy, He loves programming but he has lower CGPA.")
#============================== Play any song form hard drive using ==================================================
                if user == "music please" or user=="Music please":
                        song()
#========================== Empty Recycle bin==========================================================================
                if user == "empty recycle bin" or user == "recycle bin":
                        speak("ok sir.")
                        empty()
                        speak("recycle bin empty process is complete sir")
#=========================== Lock Computer ==========================================================================
                if user == "lock my computer":
                        speak("Definately sir i will lock your computer so that no one can access it.")
                        ctypes.windll.user32.LockWorkStation()
#================================ Take screen shot ======================================================================
                if user == "take screenshot" or user == "screenshot":
                        speak("Ok sir, i will take screen shot and save it to desktop")
                        pic = pyautogui.screenshot()
                        pic.save('Screenshot.png')
                        speak("Screen shot has been saved.")
#=============================== Google search using "search ________" ==========================================
                if user[0:6]=="search":
                        a = user[7:len(user)]
                        open_google(a)
#================================== Find any location using "where is ________ " =====================================
                if user[0:8]=="where is":
                        a = user[9:len(user)]
                        url = "https://www.google.co.in/maps/place/"+a
                        webbrowser.open_new(url)
#============================ Open YouTube =====================================================
                if user=="open YouTube" or user=="YouTube" or user=="youtube":
                        webbrowser.open_new("https://www.youtube.com/?gl=IN")
#============================ Open GMail =====================================================
                if user=="open Gmail" or user=="GMail" or user=="gmail" or user=="open gmail":
                        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
#========================== Open folders that are already in hard drive (All folders are in my computer.It won't work for you)==============================================
                if user=="open movies":
                        os.startfile("E://Movies")
                if user=="open software":
                        os.startfile("F:\\Software !")
                if user=="open wallpaper":
                        os.startfile("F:\\Wallpaper")
                if user=="open videos":
                        os.startfile("E:\\video")
                if user=="open songs" or user=="open song":
                        os.startfile("F:\\Favourites")
                if user=="open my projects" or user=="open my project":
                        os.startfile("G:\\")
#============================ Open facebook ====================================================
                if user=="open Facebook" or user=="open fb" or user=="open my fb account":
                        webbrowser.open_new("https://www.facebook.com/")
#============================ Google search about something using "what is ____" =========================
                if user[0:7]=="what is":
                        a = user[8:len(user)]
                        if a!= "your name":
                                open_google(a)
#============================== Google search about a famous person using "who is_____" ===========================
                if user[0:6]=="who is":
                        a = user[7:len(user)]
                        if a!= "Pankaj" or a!= "pankaj":
                                open_google(a)
#============================== Play any song or vedio on You Tube using "play ______" ====================================
                if user[0:4]=="play" or user[0:4]=="Play":
                        a = user[5:len(user)]
                        research_later = a+" on youtube"
                        speak("Playing "+a+" on web.")
                        goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
                        k = requests.get(goog_search)
                        soup = BeautifulSoup(k.text, "html.parser")
                        webbrowser.open_new(soup.find('cite').text)#searches a song as"song on youtube"&opens first link
#=================================== Download a video on youtube using "Download ____________ " =================
                if user[0:8] == "Download" or user[0:8]=='download':
                        a = user[9:len(user)]
                        research_later = a+" on youtube"
                        print("Downloading is on process........Please wait.")
                        goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
                        k = requests.get(goog_search)
                        soup = BeautifulSoup(k.text, "html.parser")
                        YouTube(soup.find('cite').text).streams.first().download()
#============================= Search Some thing on WikiPedia using "wiki __________"=======================================================
                if user[0:4] == "wiki" or user[0:4] == "Wiki" or user[0:5]=="Vicky":
                        a = user[5:len(user)]
                        url = "https://en.wikipedia.org/wiki/"+a
                        webbrowser.open_new(url)
#============================ Open Coursera ======================================================
                if user=="open coursera" or user=="Open Coursera" or user=="Coursera":
                        webbrowser.open_new("https://www.coursera.org/learn/machine-learning/home/welcome?utm_medium=email&utm_source=other&utm_campaign=opencourse.welcome.machine-learning.~opencourse.welcome.Gtv4Xb1-EeS-ViIACwYKVQ.")                                        
#=============================== Check Pyro can hear you or not =============================================
                if user=="can you hear me":
                        speak("yes, you are coming in loud and clear ")
#========================== When error occurs in listening ================================
        except sr.UnknownValueError:
                print("Sorry ! Could not understand audio.Can you speak again please sir?")
        except sr.RequestError as e:
                print("Recog Error; {0}".format(e))
#============================= Starting body =============================================
if(int(localtime[11:13])<12):
        speak("Good morning pankaj")
elif(int(localtime[11:13])>12 and int(localtime[11:13])< 17):
        speak("Good afternoon pankaj")
else :
        speak("Good evening pankaj")
speak("how can i help you?")
#======================== Main class defined ===========================================
if __name__ == "__main__":
        r = sr.Recognizer()
        with sr.Microphone() as source:
                while 1:
                        mainfunction()
#======================== PROGRAM END ======================================================

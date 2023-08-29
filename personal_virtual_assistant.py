import pyttsx3 #to convert your all talking into a text
import speech_recognition as sr #to recognize speech
import pywhatkit #to open YouTube
import pyjokes #to get some jokes
import wikipedia
import datetime #for current time
import webbrowser #to any website
import os  #to open file location we use os
import random
from win32com.client import Dispatch
import requests
import pyautogui
import json
import urllib
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
from bs4 import BeautifulSoup
import googletrans

print("hey user! you can this jarvis to \n1: jarvis play music\n2: \"jarvis wikipedia of\" some person or \"who is\" some person\n3: jarvis open youtube\n4: jarvis open gmail\n5: jarvis open google\n6: send whatsapp message\n7: jarvis game\n8: jarvis jokes\n9: jarvis what is the time\n10: jarvis what is your name\n11: jarvis what is my name\n12: jarvis stop(to end)\n13:jarvis take a note\n14:weather")
listener=sr.Recognizer()
engine=pyttsx3.init() #intialalizing pyttsx3

def talk(text):
    engine.say(text) #to talk
    engine.runAndWait() #to wait for user to talk

hour = datetime.datetime.now().hour

Windows_Speak = Dispatch('SAPI.Spvoice')

Windows_Speak.Rate = 2
# to see the current hour based on that wishing
if (hour > 0 and hour < 12):
   rand_ans = ["good morning sir,this is alexa here, how may i help you",
               "HOLA, what can i do for you?"]
   b = random.sample(rand_ans, k=1)
   Windows_Speak.Speak(b)
elif(hour>=12 and hour<=15):
   rand_ans = ["good afternoon sir,this is alexa here, how may i help you",
               "HOLA, what can i do for you?"]
   b = random.sample(rand_ans, k=1)
   Windows_Speak.Speak(b)
else:
   rand_ans = ["good evening sir,this is alexa here, how may i help you",
               "HOLA, what can i do for you?"]
   b = random.sample(rand_ans, k=1)
   Windows_Speak.Speak(b)

def take_command():
    try:
        with sr.Microphone(device_index=0) as source: #triggers and open microphone
            print("listening......")
            listener.pause_threshold=1496.57047568
            voice=listener.listen(source,timeout=5,phrase_time_limit=5)
            command=listener.recognize_google(voice) #google talk engine is good so we use it
            command=command.lower() #converting every text spoken into smaller case
            if("jarvis" in command ):
                command=command.replace("jarvis","") #replacing jarvis to print command
                print(command) #triggers only if jarvis is there in speech
    except:
        pass
    return command


def run_jarvis():
    command=take_command()
    if("play" in command):
        song=command.replace("play","")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    elif("joke" in command):
        talk(pyjokes.get_joke())
    elif("google search" in command or "what is" in command):

        import wikipedia as googleScrap
        talk("this is what I found on the web")
        try:
            sp = command.replace("google search", "")
            pywhatkit.search(sp)
            result=googleScrap.summary(sp,1)
            talk(result)
        except:
            talk("could not search in web")


    elif("wikipedia" in command or "who is" in command):
        if("wikipedia" in command):
            wiki=command.replace("wikipedia","")
            info=wikipedia.summary(wiki,2)
            print(info)
            talk(info)
        elif("who is" in command):
            person=command.replace("who is","")
            data=wikipedia.summary(person,2)
            print(data)
            talk("according to wikipedia")
            talk(data)

    elif("time" in command):
        time=datetime.datetime.now().strftime("%I:%M %p") #%I is for 1-12 timings if i make %H then it will take from 1-24
        #M is for minute and #S is for second that we didn't add but still to know about it
        #p is for knowing is it am or pm
        talk(f"the current time is {time}")
        print(time)

    elif ("silent stop" in command or "stop silently" in command):
        exit()

    elif("stop" in command):
        talk("okay  sir")
        talk("it was a good time with you")
        talk("jarvis is signing off bye bye")
        exit()

    elif("how are you" in command):
        rand_ans=["i a am very good sir, how about you","pleasure, you asked about it, i am very good, and hope your doing well"]
        b=random.sample(rand_ans,k=1)
        talk(f"{b}")
    elif("like" in command):
        talk("i just like myself and nothing else")
    elif("what is your name" in command or "who are you" in command):
        rand_ans=["i am someone ,who is bored by, answering your question, any ways, i am jarvis","i am your jarvis, ready to help you all time, let me know if you need any help","you woked me up from sleep, for asking this, anyways i am jarvis, but not a slave","i am cheap jarvis, and i can do anything for you"]
        b=random.sample(rand_ans,k=1)
        talk(f"{b}")
    elif("what is my name" in command):
        talk("i am not very sure, but i had heard people calling you, the legend")
        talk("and luckily we both are, talking")
    elif("open youtube" in command):
        op=command.replace("open","")
        talk("opening"+ op)
        webbrowser.open("youtube.com")
    elif("open google" in command):
        sp=command.replace("open","")
        talk("opening"+sp)
        webbrowser.open("google.com")
    elif("open gmail" in command):
        pp=command.replace("open","")
        talk("opening"+pp)
        webbrowser.open("gmail.com")
    elif("open pycharm" in command):
        address="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
        talk("opening pycharm")
        os.startfile(address)

    elif ("whatsapp" in command):
        if ("send a" in command):
            op = command.replace("send a", "").replace("whatsapp message to", "")
            talk(f"what message should i send to {op}")
            print(op)
            g = take_command()

            import time
            pyautogui.click(x=825, y=1053)
            time.sleep(3)
            pyautogui.click(x=118, y=141)
            pyautogui.write(op)
            time.sleep(1)
            pyautogui.click(x=384, y=304)
            pyautogui.click(x=965, y=983)
            pyautogui.write(g)
            talk("message will be sent in 5 seconds")
            time.sleep(5)
            pyautogui.click(x=1869, y=974)
            talk("message sent succesfully")
            pyautogui.click(x=1781, y=13)
        elif ("send" in command):
            op = command.replace("send", "").replace("whatsapp message to", "")
            talk(f"what message should i send to {op}")
            print(op)
            g = take_command()

            import time
            pyautogui.click(x=825, y=1053)
            time.sleep(3)
            pyautogui.click(x=118, y=141)
            pyautogui.write(op)
            time.sleep(1)
            pyautogui.click(x=384, y=304)
            pyautogui.click(x=965, y=983)
            pyautogui.write(g)
            talk("message will be sent in 5 seconds")
            time.sleep(5)
            pyautogui.click(x=1869, y=974)
            talk("message sent succesfully")
            pyautogui.click(x=1781, y=13)
        elif ("whatsapp" in command):
            op = command.replace("whatsapp", "")
            talk(f"what message should i send to {op}")
            print(op)
            g = take_command()

            import time
            pyautogui.click(x=825, y=1053)
            time.sleep(3)
            pyautogui.click(x=118, y=141)
            pyautogui.write(op)
            time.sleep(1)
            pyautogui.click(x=384, y=304)
            pyautogui.click(x=965, y=983)
            pyautogui.write(g)
            talk("message will be sent in 5 seconds")
            time.sleep(5)
            pyautogui.click(x=1869, y=974)
            talk("message sent succesfully")
            pyautogui.click(x=1781, y=13)

    elif("maths" in command):
        talk("write ur numbers below")
        a=eval(input("write here: "))
        talk(f"your answer is {a}")
        print(a)

    elif(" game" in command):
        talk("getting bored, its okay,lets play something")

        talk("there are number from 1 to 10, and you have to guess")
        talk("which one i was thinking of")

        gm=random.randint(1,10)
        talk("okay now guess you number")
        user=int(input("guess your number"))
        if(user==gm):
            talk("congratulation sir, your born genius")
            print("correct")
        else:
            talk("you lost, try your luck next time")
            talk(f"the number was {gm}")
            print(f"the actual number was {gm}")
    elif("alarm" in command or "wake me" in command):
        rand_ans = ["what time should i wake you up", "when do you want to get up",
                    "when should i keep alarm for"]
        b = random.sample(rand_ans, k=1)
        talk(b)
        time=take_command()
        time=time.replace("set alarm to","")
        time=time.replace(".","")
        time=time.upper()
        import myalarm
        myalarm.alarm(time)

    elif("reminder" in command or "remind me" in command):
            talk("What you should be reminded of?")
            rememberMessage = command.replace("remind me of", "")
            talk("You told me to remember that" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage + '\n')
            remember.close()

    elif ("take a note" in command or "write a note" in command):
        talk("Tell me the Query")
        talk("I am ready to write")
        writes = take_command()
        talk("Tell me the filename")
        filename = take_command()
        with open(filename, 'w') as f:
            f.write(writes)
            done = True
            talk(f"i successfully created a note {filename}")


    elif ("temperature" in command or "weather" in command):
        if ("current" in command):
            op = command.replace("temperature", "").replace("what is the current", "")
            url = f"https://www.google.com/search?q=what is the current temperature"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            t = int(temp[:2])
            if (t > 28):
                talk(f"I Feel hot today, oh yah! because the current temperature is {temp}")
            elif (t > 19 and t >= 28):
                talk(f"It is a warm day as the current temperature is {temp}")
            elif (t <= 19 and t >= -20):
                talk(f"its cold out sidd with {temp} , so better to stay under your blanket")
        elif ("weather" in command):
            op = command.replace("weather in", "").replace("what is the", "")
            url = f"https://www.google.com/search?q=what is the temperature in {op}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            t = int(temp[:2])
            if (t > 28):
                talk(f"I Feel hot today, oh yah! because it is {temp} in {op}")
            elif (t > 19 and t >= 28):
                talk(f"It is a warm day as it is {temp} in {op}")
            elif (t <= 19 and t >= -20):
                talk(f"its cold out side with {temp} in {op}, so better to stay under your blanket")
        elif ("temperature" in command):
            op = command.replace("temperature in", "").replace("what is the", "")
            url = f"https://www.google.com/search?q=what is the temperature in {op}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            t = int(temp[:2])
            if (t > 28):
                talk(f"I Feel hot today, oh yah! because it is {temp} in {op}")
            elif (t > 19 and t >= 28):
                talk(f"It is a warm day as it is {temp} in {op}")
            elif (t <= 19 and t >= -20):
                talk(f"its cold out side with {temp} in {op}, so better to stay under your blanket")
    elif("news" in command or "headlines" in command):
        talk("These are the headlines for today:")
        import news
        news.speak_news()

    elif("command promt" in command or "cmd" in command):
        address = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\\"
        talk("opening cmd")
        os.startfile(address)

    elif("IP address" in command or "ip" in command):
        def find_my_ip():
            ip_address = requests.get('https://api64.ipify.org?format=json').json()
            return ip_address["ip"]
        talk("Your IP address is" + find_my_ip())

    elif("advice" in command or "give me a advice" in command):
        def get_random_advice():
            res = requests.get("https://api.adviceslip.com/advice").json()
            return res['slip']['advice']
        talk(get_random_advice())

    elif ("photo" in command or "turn on camera" in command or "switch on camera" in command or "camera" in command or "take my picture" in command or "click my photo" in command):
        import subprocess as sp
        if ("turn on" in command or "switch on" in command):
            sp.run('start microsoft.windows.camera:', shell=True)
        elif ("click" in command or "capture" in command):
            import time
            sp.run('start microsoft.windows.camera:', shell=True)
            talk("say cheese sir")
            pyautogui.click(x=1283, y=518, duration=1.5)
            pyautogui.moveTo(x=1304, y=24)
            time.sleep(1)
            pyautogui.click(x=1304, y=24)

    elif ("located" in command or "location" in command or "current location" in command or "find loaction" in command or "located" in command or "show me the distance" or "distance" in command or "how far is" in command):
        if("current location" in command or "tell me my current location" in command):
            url = 'http://ipinfo.io/json'
            response = urllib.request.urlopen(url)
            data = json.load(response)
            city = data['city']
            region = data['region']
            talk(f"You are now in India {city} {region}")
            exit()

        elif ("find loaction" in command or "located" in command or'located' in command or 'location' in command or "distance" in command or "how far is" in command):
            if ('located' in command or 'location' in command):
                place = command.replace("where is", "").replace("located", "")
                Url_place = "https://www.google.com/maps/place/" + str(place)
                web.open(url=Url_place)
                geolocator = Nominatim(user_agent="myGeocoder")
                location = geolocator.geocode(place, addressdetails=True)
                target_latlon = location.latitude, location.longitude
                location = location.raw['address']
                target = {'city': location.get('city', ''),
                          'state': location.get('state', ''),
                          'country': location.get('country', '')}
                talk(target)
                exit()
            elif ("distance" in command or "how far is" in command):
                place = command.replace("how far is", "").replace("city", "")
                place = place.replace("show me the distance to", "").replace("find distance of", "")
                Url_place = "https://www.google.com/maps/place/" + str(place)
                web.open(url=Url_place)
                geolocator = Nominatim(user_agent="myGeocoder")
                location = geolocator.geocode(place, addressdetails=True)
                target_latlon = location.latitude, location.longitude
                current_loca = geocoder.ip('me')
                current_latlon = current_loca.latlng
                distance = str(great_circle(current_latlon, target_latlon))
                distance = str(distance.split(' ', 1)[0])
                distance = round(float(distance), 2)
                talk(f"Sir {place} is {distance} kilometers away from your location ")
                exit()
    else:
        talk("what the hell love, be clear when you talk")
        talk("now ,can you repeat the same again properly")

while True:
    run_jarvis()





















My Alarm class:


import datetime
from playsound import playsound
def alarm(timing):
    time_a = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    time_a = time_a[11:-3]
    hor = time_a[:2]
    hor = int(hor)
    minr = time_a[3:5]
    minr = int(minr)
    print(f"done alarm is set for {timing}")

    while True:
        if hor==datetime.datetime.now().hour:
            if minr==datetime.datetime.now().minute:
                playsound('Alarm-ringtone.mp3')
            elif minr<datetime.datetime.now().minute:
                break










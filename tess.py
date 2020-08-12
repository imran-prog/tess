# Importing Modules
import pyttsx3
import speech_recognition as sr
import wikipedia, webbrowser, os, smtplib, sys, pyperclip
import time, weather_go, wishing, random, sound, keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)  # Tess Voice
engine.setProperty('rate', 173)
engine.setProperty('volume', 10)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    if 4 <= wishing.hour < 10:
        speak(wishing.morning_commands())
    elif 10 <= wishing.hour < 13:
        speak(wishing.noon_commands())
    elif 13 <= wishing.hour < 17:
        speak(wishing.afternoon_commands())
    elif 17 <= wishing.hour < 23:
        speak("Good Evening Sir! How was your day today")
    else:
        speak("Its Getting dark Sir and you are still awake, do you Need any help")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print("User Said: ", query, "\n")
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"

    return query


def open_web(web_name):
    webbrowser.open(web_name)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('infotainer04@gmail.com', '')
    server.sendmail('infotainer04@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    # wishing.security()
    while True:
        query = takeCommand().lower()

        # Logics for executing tasks based on query
        # Personal Questions
        if "who are you" in query:
            comm = ["I am Tess, and i run this house", "My name is Tess"]
            go = random.choice(comm)
            speak(go)

        elif "who made you" in query:
            comm = ["I am a creation of two best friends", "It was sir, who gave me birth"]
            go = random.choice(comm)
            speak(go)

        elif "language you are written" in query:
            speak("My Mother Language is Python")

        elif "are you up" in query:
            speak("For you Sir! Always")

        elif "thank" in query:
            speak("My pleasure Sir")

        elif "temperature" in query:
            speak(f"the temperature of islamabad is {weather_go.city_temp}")

        # Browser Working
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            print(results)
            speak(results)

        elif "goto" in query or "go to" in query:
            if "goto" in query:
                query = query.replace("goto", "")
            elif "go to" in query:
                query = query.replace("go to", "")
            speak(f'opening {query}')
            open_web(query)

        elif "search google map" in query:
            if "search google map from clipboard" == query:
                query = pyperclip.paste()
            else:
                speak("which place do you want to see")
                query = takeCommand().lower()
            speak(f"Going to {query}...")
            webbrowser.open('https://www.google.com/maps/place/' + query)

        elif "play music" in query or "my music" in query:
            open_web("https://www.youtube.com/watch?v=eqOewr6fzC8&list=PLTGYQPmpqDE836ETvP1jxV28ui3V-UbrB")

        elif query == "open Instagram":
            pass

        # System processes

        elif "the time" in query:
            strTime = wishing.time.strftime("%H:%M")
            speak(f"the time is {strTime} {wishing.time_pace()}")

        elif "start code" in query:
            codePath = "C:\\Users\\DESKTOP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open pycharm" in query:
            codePath = "D:\\Dead\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif "open microsoft edge" in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
        elif "open chrome" in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif "open control panel" in query:
            codePath = "%windir%\\System32\\Control.exe"
            os.startfile(codePath)
        elif "open sublime text" in query:
            codePath = "D:\\Dead\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        elif "open python directory" in query:
            codePath = "E:\\Python"
            os.startfile(codePath)
        elif "open python course" in query:
            codePath = "D:\\Courses V2\\[FreeCourseSite.com] Udemy - Complete Python Developer in 2020 Zero to Mastery"
            os.startfile(codePath)
        elif "open notepad" in query:
            codePath = "%windir%\\system32\\notepad.exe"
            os.startfile(codePath)
        elif "open slack" in query:
            codePath = "C:\\Users\\Anonymous\\AppData\\Local\\slack\\slack.exe"
            os.startfile(codePath)
        elif "open zoom" in query:
            codePath = "C:\\Users\\Anonymous\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)

        elif "change volume to" in query:
            query = query.replace("change volume to", "")
            sound.Sound.volume_set(int(query))
            speak("Volume changed to " + query + "percent")

        # Shortcut Keys
        elif "lock the system" in query:
            keyboard.press_and_release("win + l")
        elif "go to desktop" in query:
            keyboard.press_and_release("win + d")
        elif "open settings" in query:
            keyboard.press_and_release("win + i")
        elif "minimize all" in query:
            keyboard.press_and_release("win + m")
        elif "undo" in query:
            keyboard.press_and_release('ctrl + z')
        elif "redo" in query:
            keyboard.press_and_release("ctrl + y")
        elif "paste" in query:
            keyboard.press_and_release("ctrl + v")
        elif "copy" in query:
            keyboard.press_and_release("ctrl + c")
        elif "cut" in query:
            keyboard.press_and_release("ctrl + x")
        elif "save" in query:
            keyboard.press_and_release("ctrl + s")
        elif "start" in query:
            keyboard.press_and_release("win")
        elif "select all" in query:
            keyboard.press_and_release("ctrl + a")
        elif "go to end" in query:
            keyboard.press_and_release("ctrl + end")
        elif "save the file" in query:
            keyboard.press_and_release("ctrl + s")
        elif "application" in query:
            if "next" in query:
                keyboard.press_and_release('alt + tab')
            if "previous" in query:
                keyboard.press_and_release('alt + shift + tab')
        elif "desktop" in query:
            if "next" in query:
                keyboard.press_and_release('win + ctrl + right')
            if "previous" in query:
                keyboard.press_and_release('win + ctrl + left')

        elif "send email" in query:
            try:
                speak("What should I say")
                content = takeCommand().lower()
                to = "akbarali034@gamil.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, but this email can not be send")

        # Alwidah
        elif "shutdown the system" in query:
            speak("Do you really want to shutdown your computer sir!")
            comm = takeCommand().lower()
            if "yes" in comm:
                speak("Goodbye sir")
                os.system("shutdown /s /t 1")
            else:
                continue

        elif "logout the computer" in query:
            speak("Do you really want to logout your computer sir!")
            comm = takeCommand().lower()
            if "yes" in comm:
                speak("Goodbye sir")
                os.system("shutdown -l")
            else:
                continue

        elif "restart the system" in query or "reboot" in query:
            speak("Do you really want to restart your computer sir!")
            comm = takeCommand().lower()
            if "yes" in comm:
                speak("Goodbye sir")
                os.system("shutdown /r /t 1")
            else:
                continue

        elif "goodbye" in query or "quit" in query:
            speak("Good Bye Sir have sweet dreams")
            exit()

        time.sleep(10)
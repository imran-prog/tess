from locate_me import location_of_me
from datetime import datetime
import weather_go
import random
from tess import speak

time = datetime.now()
# print(time) >  2020-08-09 21:19:07.071096 > %d/%m/%Y %H:%M:%S

hour = int(time.strftime('%H'))


def time_pace():
    if 0 <= hour <= 12:
        return "a m"
    else:
        return "p m"


def security():
    while True:
        speak("Enter the username to get access in Network")
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        if username == "tess123" and password == "qwerty":
            speak("Hello Sir! You have got access to the network")
            break
        else:
            speak("You are not authorized to access this area.")
            continue


def morning_commands():
    stat = ["increasing gradually", "decreasing"]
    morning = f"Good Morning. It's {hour} A.M. The weather in {location_of_me()} is {weather_go.city_temp} with {weather_go.city_weather}. The wind speed is {weather_go.city_wind_speed} and {random.choice(stat)}, and your exercise time will be starting in 30 minutes "

    return morning

def noon_commands():
    comm = ["Sir what you want today for your lunch", "What are you main goals today", "Sir Today you got a meeting at 5 P.M", "How was your breakfast Sir!", "Are you working today on new project or want to take on the previous one", "Do you want brunch or want to do lunch only today"]
    noon = random.choice(comm)

    return noon

def afternoon_commands():
    comm = ["Good Afternoon Sir!", "How was your launch today", "what would you take in dinner Sir", "sir do you want to know your next schedule"]
    afternoon = random.choice(comm)

    return afternoon


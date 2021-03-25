import time
import datetime
import stats as s
import sys
import json
from datetime import date

def start_up():
    print("Good morning! What would you like to do? \n")
    user_choice()

def user_choice():
    command = input("work on a task (type \"task\")\ncheck your stats (type \"stats\") \n ")
    if command == "task":
        check_task()
    if command == "stats":
        s.get_stats()
    else: 
        print("illegal input, please try again")
        user_choice()

def check_task(): 
    category = input("Which category are you working in? Your options are \n work \n fun \n waste \n")
    print("great! Get to work, just tell me when you're done.")
    timer(category)

def timer(category):
    startTime = time.time()
    response = input("are you done working? y/n \n")
    time_log(category, startTime)

    
    
def time_log(category, startTime):
    data = (time.time() - startTime)
    timeInt = int(data)

    save_time(category, timeInt)
    #print("you worked for", timeInt, "seconds in category", category) # det här är raden som ska bort och bli sparad tid istället


def repeat():
    again = input("would you like to do something else? y/n \n")
    if again == "y":
        user_choice()
    if again == "n":
        sys.exit()


def save_time(category, timeInt): #TODO: konvertera timeInt till minuter
    minutes = (timeInt / 60)
    minutesConverted = round(minutes, 2)
    with open('timeLog.json', 'r+') as f:
        taskInput = ", \n" + "{" + "\"category\": \"{}\", \"timeInMinutes\": {}".format(category, minutesConverted) + "}"
        s = f.read()
        index = s.rfind("]")
        f.seek(index)
        f.write(taskInput)
        f.write(s[index:])
    
    repeat()

def test(category, timeInt):
    taskInput = ", \n" + "{" + "\"category\": \"{}\", \"timeInMinutes\": {}".format(category, timeInt) + "}"
    print(taskInput)


start_up()
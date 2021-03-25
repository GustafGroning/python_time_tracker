import time
import datetime
import stats as s
import sys
import json
from datetime import date

def start_up():
    print("Hi! What would you like to do? \n")
    user_choice()

def user_choice():
    command = input("work on a task - type \"task\"\ncheck your stats - type \"stats\" \n \n ")
    if command == "task":
        check_task()
    if command == "stats":
        s.get_stats()
        repeat()
    else: 
        print("\nillegal input, please try again: \n \n")
        user_choice()

def check_task(): 
    categoryList = ["work", "fun", "waste"]
    category = input("Which category are you working in? Your options are \nwork \nfun \nwaste \n \n")
    if category not in categoryList:
        print("\nThat's not a valid category, please try again!\n")
        check_task()
    else:
        print("\ngreat! Get to work, just tell me when you're done.")
        timer(category)

def timer(category):
    startTime = time.time()
    input("\nType \"y\" whenever you've done with this task \n")
    time_log(category, startTime)

def time_log(category, startTime):
    data = (time.time() - startTime)
    timeInt = int(data)
    save_time(category, timeInt)

def repeat():
    again = input("Would you like to do something else? y/n")
    if again == "y":
        user_choice()
    if again == "n":
        print("\n Bye for now!")
        sys.exit()
    if again not in "y" or "n":
        print("\n illegal input, please try again \n")
        repeat()

def save_time(category, timeInt):
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

start_up()
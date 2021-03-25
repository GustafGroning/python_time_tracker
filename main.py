import time
import datetime
#import stats as s
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

    print("you worked for", timeInt, "seconds in category", category) # det här är raden som ska bort och bli sparad tid istället


    again = input("would you like to do something else? y/n \n")
    if again == "y":
        user_choice()
    if again == "n":
        sys.exit()

def save_time():
    # load from file
    a_dictionary = {"category": "TESTING", "timeInMinutes": 400}
    with open('timeLog.json','r+') as f:
        dic = json.load(f)
        dic.update(a_dictionary)
        json.dump(dic, f)

def time_test():
    with open('timeLog.json', 'r+') as f:
        s = f.read()
        index = s.rfind("]")
        f.seek(index)
        f.write(',\n {"category": "fun", "timeInMinutes": 20} \n')
        f.write(s[index:])
  #{"category": "work", "timeInMinutes": 40} är hur formatet ska se ut när det är färdigt.

time_test()
#save_time()
#start_up()
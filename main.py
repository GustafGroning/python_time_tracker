import time
import datetime
import stats as s

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
    dataInt = int(data)
    print(data)
    print(dataInt)
    print("you worked for", dataInt, "seconds in category", category)

start_up()

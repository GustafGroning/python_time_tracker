import time
from appkit import NSWorkspace


testList = ["Trello", "Safari"]
def check_window(): 
    first_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    while True:
        new_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        if new_window != first_window:
            check_category(new_window)
        else:
            print("no change")
            time.sleep(1)

    
def check_task(): 
    category = input("Which category are you working in? Your options are \n work \n hobbies \n unproductive \n")
    print("Great! Get to work, just type " + "stop" + "when you are done.")


    
"""
1. ta in kategori
2. printa "great! Get to work, just type "stop" when you are done.
3. skriver "stop", spara tiden.
"""



def timer():
    start_time = time.time()
    while True:
        try:
            print("tjena!")
            #elapsed_time = time.time() - start_time
            time.sleep(1)
        except:
            raise KeyboardInterrupt
            break





timer()


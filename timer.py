
import time
import main as m
from AppKit import *

def timer(new_window, category):
    start_time = time.time()
    while True:
        newer_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        elapsed_time = time.time() - start_time

        if new_window != newer_window:
            print("you spent", elapsed_time, "in trello, good job!")
            m.check_window()
        else:
            time.sleep(1)
    
#timear sekunder som användaren är i fönstret
#om användaren byter fönster, skicka till time_log

def time_log():
    pass

# spara tid spenderad och kategori i JSON
# skicka till check_window

import webbrowser
import ezmaker
import pyautogui
import time


print ('''____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
                                                                             ''')



def open():
    webbrowser.open("google.com")

def spam():
    spad = input("Tesxt to spam: ")

    time.sleep(5)
    for i in range (500):
        
        pyautogui.typewrite(spad)
        pyautogui.press("enter")

def tkinter():
    ezmaker.easyui3butn('500x500', 'title', 'lounch', 'cs', 'cs', open)



def meno():
    ezmaker.meno()



name = input('Enter name: ')
if name == ("Ghost"):
    print("Welcome Creator")
    
    

while True:
   


    


    command = input(f"{name}>: ")

    if command == ("win"):

        tkinter()
   
    if command == ("spam"):
        spam()
  
    if command == ("namegame"):
        meno()



    if command == ("web"):
         open()



    if command == ("info"):
        print('version: 0.0.1  by GhostPingu')

    if command == ("quit"):
        quit()


  
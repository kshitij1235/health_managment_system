#pakages

import webbrowser
import time
import os
import pyttsx3
from plyer import notification
import random
import tkinter as tk
from tkinter import *
import os 




# functions 


def countdown(t):
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1
  
      
def work():
    noti = 0
    watch = 0
    sec = 0
    # variables for shedules
    drink = int(water.get()) #1200
    alert = int(eye.get())   #300
    exercise = int(exercise_eye.get())    #1800
    stop = int(stop_using.get())    #28800
    rest= int(rest1.get())#600
    d=int(water.get())#1200
    a=int(eye.get())#300
    e=int(exercise_eye.get())#1800
    r=int(stop_using.get())#600
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say("WELCOME TO HEALTH MANAGEMENT SYSTEM , we have set  all best for you so dont worry ")
    engine.runAndWait()
    print("WELCOME YOU HAVE STARTED WITH HEALTH MANAGEMENT SYSTEM")
    print("\nsetting up few things......")
        
    print("\nstarting timer.......")
    time.sleep(1)
    print("Timer started...")
    print("\n--------------------------------------------")
    notification.notify(title="welcome", message="welcome to health managment system", timeout=10)
    while(0 == 0):
        sec=sec+1
        countdown(sec)
        watch=watch+1
        if alert == sec:
            noti = noti+1
            print("notification for alert for your eyes")
            print("\ntotal notification", noti)
            print("time taken",watch,"sec")
            print("\n--------------------------------------------")
            notification.notify(
                title="ALERT!!!!", message="keep your eyes away from the screen", timeout=10)
            engine.say("please keep your away")
            engine.runAndWait()
            alert = alert + a
        if rest == sec:
            noti = noti+1
            print("notification for rest")
            print("\ntotal notification", noti)
            print("time taken",watch,"sec")
            print("\n--------------------------------------------")
            notification.notify(
                title="Take Some Rest", message="take some rest", timeout=10)
            engine.say("take some rest")
            engine.runAndWait()
            rest = rest + r
        if drink == sec:
            noti = noti+1
            print("total notification", noti)
            print("\n--------------------------------------------")
            notification.notify(
                title="DRINK WATER", message="take some rest and drink water", timeout=10)
            engine.say("please drink some water")
            engine.runAndWait()
            drink = drink + d
        if exercise == sec:
            noti = noti+1
            print("notification for exercise")
            print("total notification", noti)
            print("\n--------------------------------------------")
            notification.notify(title="PLEASE DO EXCERCISE",
                                message="please start with eye exercise", timeout=10)
            engine.say("please keep your away")
            engine.runAndWait()
            exercise = exercise + e
        if stop == sec:
            noti = noti+1
            print("notification for stop your computer")
            print("total notification", noti)
            print("\n--------------------------------------------")
            notification.notify(
                title="STOP!!!!", message="you had your day please close you computer", timeout=10)
            engine.say("please stop working right now u had enough of your")
            engine.runAndWait()
            print('DO YOU WANT TO SHUT DOWN YOUR PC(y/n)??')
            user = str(input(">>> "))
            if user in ["yes", "y", "Y", "Yes", "YES"]:
                os.system("shutdown /s /t 1")
            if user in ["no", "n", "N", "No", "NO"]:
                print("please stop if u can")
                break
            
                   
#programs       
   
root = Tk()

#TITLE
root.title("HEALTH MANAGEMENT SYSTEM")

#color of background
root.config(bg="white")

#SCREENSIZE
root.geometry("300x200")
root.minsize(300,300)
root.maxsize(300,300)


# datatype of menu text

#heading 
var=StringVar()
label = Label( root, textvariable=var, bg="white" )
var.set("WELCOME TO HEALTH MANAGEMENT SYSTEM")
label.pack()


lab1=Label(root,text="Enter values in seconds")
lab1.place(y=40,x=1)

lab1=Label(root,text="Mainting eye distance : ")
lab1.place(y=70,x=1)
eye=Entry(root)
eye.insert(END, '300')
eye.place(y=70,x=150)

lab2=Label(root,text="Drinking water : ")
lab2.place(y=100,x=1)
water=Entry(root)
water.insert(END, '1200')
water.place(y=100,x=150)

lab2=Label(root,text="eye exercise :")
lab2.place(y=130,x=1)
exercise_eye=Entry(root)
exercise_eye.insert(END, '1800')
exercise_eye.place(y=130,x=150)

lab2=Label(root,text="stop using :")
lab2.place(y=160,x=1)
stop_using=Entry(root)
stop_using.insert(END, '2800')
stop_using.place(y=160,x=150)

lab2=Label(root,text="rest :")
lab2.place(y=190,x=1)
rest1=Entry(root)
rest1.insert(END, '600')
rest1.place(y=190,x=150)

B = tk.Button(root, text ="Play", command = work) 
B.place(x=110, y=250)

root.mainloop()

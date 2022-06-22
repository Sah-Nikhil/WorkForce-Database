#directory import
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os

import sticky as sticky
from PIL import ImageTk


#create root as base of software
from turtle import width, fillcolor

root = tk.Tk()
root.title("Workforce Database Home")
root.geometry("640x447")
root.configure(bg='black')
root.resizable(False ,False)
root.iconbitmap("logo.ico")

#background image set
bg = ImageTk.PhotoImage(file="loginimg.png")

#canvas background image setup
canvas = Canvas(root, height=447, width=640, bd=0,highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,image=bg,anchor="nw")





#defining addworker
def login():
    os.system('login.py')
#defining removeworker
def register():
    os.system('register.py')


#creating buttons for interaction with the software:
#add + remove
button1 = tk.Button(root, text="REGISTER", font=("Agency FB", 11), width=10, fg="black", bg="white",relief=RAISED, command=register)
login_button_window = canvas.create_window(288, 191, anchor="nw", window=button1)


button2 = tk.Button(root, text="LOGIN", font=("Agency FB", 11), width=10, fg="black", bg="white",relief=RAISED, command=login)
login_button_window = canvas.create_window(288, 231, anchor="nw", window=button2)

#setup exitbutton
exitbutton = tk.Button(canvas,width=4, height=1, text="exit", fg="black", bg="white",anchor="nw",font=("Agency FB",9), relief=RAISED, bd=3, command=root.destroy)
exitbutton.grid(row=0, column=0, padx=3, pady=3)

#emoji: \U0001F604

#run the root
root.mainloop()
#this runs fine (this page)
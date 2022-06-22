import json
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog, Text
import os

import sticky as sticky
from PIL import ImageTk

#create root as base of software
from turtle import width, fillcolor

root = tk.Tk()
root.title("Login")
root.geometry("640x447")
root.configure(bg='black')
root.resizable(False ,False)
root.iconbitmap("logo.ico")

#creat json dictionary
accounts = {}
#username variable
un = tk.StringVar(root,'')
#password variable
pw = tk.StringVar(root,'')

#background image set
bg = ImageTk.PhotoImage(file="loginimg.png")

#canvas background image setup
canvas = Canvas(root, height=447, width=640, bd=0,highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,image=bg,anchor="nw")

# create ring function
def ring():
    root.bell()


# Create welcome screen
def welcome():
    global accounts, un, pw
    with open("accounts.json", "r+") as acc:
        accounts = json.load(acc)
    if un.get() in accounts.keys():
        if accounts[un.get()] == pw.get():
            os.system('main_yt.py')
            un_entry.destroy()
            pw_entry.destroy()
            login_button.destroy()
        else:
            canvas.create_text(319, 218, text="Login Unsuccessful! Kindly RETRY.", font=("Agency FB", 21),fill="white")
            un_entry.destroy()
            pw_entry.destroy()
            login_button.destroy()
            ring()
    else:
        canvas.create_text(319, 218, text="Account not found! Kindly RETRY.", font=("Agency FB", 21), fill="white")
        un_entry.destroy()
        pw_entry.destroy()
        login_button.destroy()
        ring()




#username + password entryboxes setup
un_entry = Entry(root, font=("Agency FB", 15), width=14, fg="#336d92", bd=0.5, textvariable=un)
pw_entry = Entry(root, font=("Agency FB", 15), width=14, fg="#336d92", bd=0.5, textvariable=pw)
un_entry.insert(0, "username")
pw_entry.insert(0, "password")

# Add the entry boxes to the canvas
un_window = canvas.create_window(260, 191, anchor="nw", window=un_entry)
pw_window = canvas.create_window(260, 231, anchor="nw", window=pw_entry)



# Define entry_clear function
def entry_clear(e):
    if un_entry.get() == 'username' or pw_entry.get() == 'password':
        un_entry.delete(0, END)
        pw_entry.delete(0, END)
        # change text to stars
        pw_entry.config(show="*")


# Bind the entry boxes
un_entry.bind("<Button-1>", entry_clear)
pw_entry.bind("<Button-1>", entry_clear)


#setup the Login Button
login_button = Button(root, text="LOGIN", font=("Agency FB", 11), width=10, fg="#336d92", command=welcome)
login_button_window = canvas.create_window(288, 271, anchor="nw", window=login_button)

#setup exitbutton
exitbutton = tk.Button(canvas,width=4, height=1, text="exit", fg="black", bg="white",anchor="nw",font=("Agency FB",9), relief=RAISED, bd=3, command=root.destroy)
exitbutton.grid(row=0, column=0, padx=3, pady=3)


#run the root
root.mainloop()
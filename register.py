import json
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
import sticky as sticky
from PIL import ImageTk


#create root as base of software
from turtle import width, fillcolor

root = tk.Tk()
root.title("Register")
root.geometry("640x447")
root.configure(bg='black')
root.resizable(False, False)


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


# Create welcome
def doneok():
    global accounts, pw, un
    with open("accounts.json", "r+") as acc:
        accounts = json.load(acc)
    accounts[un.get()] = pw.get()
    json.dump(accounts, open("accounts.json", "w+"), indent=4)
    un_entry.destroy()
    pw_entry.destroy()
    register_button.destroy()
    # Add a welcome message
    canvas.create_text(319, 218, text="Registration Successfull! Kindly EXIT. \U0001F604", font=("Agency FB", 21), fill="white")



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
register_button = Button(root, text="REGISTER", font=("Agency FB", 11), width=10, fg="#336d92", command=doneok)
register_button_window = canvas.create_window(288, 271, anchor="nw", window=register_button)

#setup exitbutton
exitbutton = tk.Button(root, text="EXIT", font=("Agency FB", 9), width=7, fg="#336d92", command=root.destroy)
exitbutton_window = canvas.create_window(10, 10, anchor="nw", window=exitbutton)


#run the root
root.mainloop()

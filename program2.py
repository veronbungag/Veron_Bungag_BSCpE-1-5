import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Program 2")
root.geometry("300x300")
root.config(background = "pink")
    
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    
    resultPopup = Toplevel(root, bg="pink")
    resultPopup.title("Result")
    
    name_label = Label(resultPopup, text=f"Name: {name}", font="Times", bg="pink" )
    name_label.pack()
    
    age_label = Label(resultPopup, text=f"Age: {age}", font="Times", bg="pink")
    age_label.pack()
    
    address_label = Label(resultPopup, text=f"Address: {address}", font="Times", bg="pink")
    address_label.pack()
    
    
label = tk.Label(root, text="PERSONAL INFORMATION", font="Times 20", bg="pink").grid(row=0, column=3)

name = tk.Label(root, text="Name", font="Courier", bg="pink")
age = tk.Label(root, text="Age", font="Courier", bg="pink")
address = tk.Label(root, text="Address", font="Courier", bg="pink")

name.grid(row=1, column=2)
age.grid(row=2, column=2)
address.grid(row=3, column=2)

name_value = StringVar
age_value = StringVar
address_value = StringVar 
check_value = IntVar

name_entry = Entry(root, textvariable =name_value)
age_entry = Entry(root, textvariable =age_value)
address_entry = Entry(root, textvariable =address_value)

name_entry.grid(row=1, column=3)
age_entry.grid(row=2, column=3) 
address_entry.grid(row=3, column=3)

check_btn = Checkbutton(text="I accept the terms and conditions.",font="Courier", bg="pink", variable= check_value)
check_btn.grid(row=6, column=3)


Button(text="Submit",font="Times", command=submit_form).grid(row=7, column=3)
root.mainloop()

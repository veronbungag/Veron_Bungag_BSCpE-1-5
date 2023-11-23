import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Program 3.1")
root.geometry("900x200")
root.config(background = "yellow")

def buy_form():
    apples = int(apple_entry.get())
    oranges = int(orange_entry.get())

    apple_price = 20
    orange_price = 25

    total_amount = (apples * apple_price) + (oranges * orange_price)

    result_text = f"Total amount to pay: {total_amount} pesos"

    resultPopup = tk.Toplevel(root, bg="yellow")
    resultPopup.title("TOTAL AMOUNT")
    
    result_label = tk.Label(resultPopup, text=result_text, font="Times", bg="yellow", justify='center')
    result_label.pack()
    
label = tk.Label(root, text="WELCOME TO RVB FRUIT STORE", font="Times 20", bg="yellow")
label.grid(row=0, column=3)

apple = tk.Label(root, text="How many apples do you want?", font="Courier", bg="yellow")
orange = tk.Label(root, text="How many oranges do you want?", font="Courier", bg="yellow")

apple.grid(row=1, column=2)
orange.grid(row=2, column=2)

apple_value = tk.StringVar()
orange_value = tk.StringVar()
check_value = tk.IntVar()

apple_entry = tk.Entry(root, textvariable =apple_value)
orange_entry = tk.Entry(root, textvariable =orange_value)

apple_entry.grid(row=1, column=3)
orange_entry.grid(row=2, column=3) 

button = tk.Button (text="BUY",font="Times", command=buy_form).grid(row=7, column=3)
root.mainloop()  
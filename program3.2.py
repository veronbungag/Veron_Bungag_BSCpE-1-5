import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Program 3.2")
root.geometry("900x200")
root.config(background = "orange")

def calculate_max_apples():
    try:
        amount_of_money = int(amount_of_money_entry.get())
        apple_price = int(apple_price_entry.get())
        
        max_apples = int(amount_of_money / apple_price)
        remaining_money = amount_of_money - (max_apples * apple_price)

        result_text = f"Maximum number of apples that you can buy: {max_apples}\nRemaining money: {remaining_money} pesos"
        resultPopup = tk.Toplevel(root, bg="orange")
        resultPopup.title("Result")

        result_label = tk.Label(resultPopup, text=result_text, font="Times", bg="orange", justify='left')
        result_label.pack()
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

label = tk.Label(root, text="WELCOME TO RVB FRUIT STORE", font="Times 20", bg="orange")
label.grid(row=0, column=3)

amount_of_money_label = tk.Label(root, text="Enter the amount of money you have:", font="Courier", bg="orange")
amount_of_money_label.grid(row=1, column=2)

apple_price_label = tk.Label(root, text="Enter the price of an apple:", font="Courier", bg="orange")
apple_price_label.grid(row=2, column=2)

amount_of_money_entry = tk.Entry(root)
amount_of_money_entry.grid(row=1, column=3)

apple_price_entry = tk.Entry(root)
apple_price_entry.grid(row=2, column=3) 

button = tk.Button(text="CALCULATE",font="Times", command=calculate_max_apples)
button.grid(row=3, column=3)
root.mainloop() 
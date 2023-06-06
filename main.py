'''
from tkinter import *

def back_to_main_window():
  window = Tk()
  window.title('Lern messagebox')
  window.geometry("500x500")
  
  Button(window, text="create new window", command=create_window).pack()
  
  window.mainloop()

def create_window():
  new_window = Toplevel()
  new_window.geometry("500x250")

  Label(new_window, text="I am a new window").pack()
  Button(new_window, text="back to main window", command=back_to_main_window).pack()

window = Tk()
window.title('Lern messagebox')
window.geometry("500x500")

Button(window, text="create new window", command=create_window).pack()

window.mainloop()
'''

from transaction import Transaction

transaction_1 = Transaction("Amazon","111","120.50","20","23/05/2023")
print(transaction_1.name)
print(transaction_1.id)
print(transaction_1.price)
print(transaction_1.amount)
print(transaction_1.date)

transaction_1.bought()
transaction_1.sold()

from transaction import Transaction
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

def buy():
  
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)

  transaction = Transaction(name,id,price,amount,date)
  file = open("buy.csv", "a", newline="")
  file.write(transaction.name + ";")
  file.write(transaction.id + ";")
  file.write(transaction.price + ";")
  file.write(transaction.amount + ";")
  file.write(transaction.date + "\n")
  print(transaction.name)
  print(transaction.price)
  print(transaction.amount)


 
def sell():
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)

  transaction = Transaction(name,id,price,amount,date)
  print(transaction.name)
  print(transaction.price)
  print(transaction.amount)

  
  
#screen label defnition and positon
stockname_text = Label(text = "Name of Stock *")
stockid_text = Label(text = "Stock ID (WKN / ISIN) ")
stockprice_text = Label(text = "Price per Share (in Euro) *")
stockamount_text = Label(text = "Amount *")
stockdate_text = Label(text = "Date of Transaction (DD/MM/YYYY) *")
stockname_text.place(x = 15, y = 70)
stockid_text.place(x = 270, y = 70)
stockprice_text.place(x = 15, y = 140)
stockamount_text.place(x = 270, y = 140)
stockdate_text.place(x = 15, y = 210)

#screen entry definition and position
stockname = Entry()
stockid = Entry()
stockprice = Entry()
stockamount = Entry()
stockdate = Entry()
stockname.place(x = 15, y = 100)
stockid.place(x = 270, y = 100)
stockprice.place(x = 15, y = 170)
stockamount.place(x = 270, y = 170)
stockdate.place(x = 15, y = 240)

Button(window, text="create new window", command=create_window).pack()

#screen button to buy or sell or do a single stock query

buy_btn = Button(window, text ="Buy", command=buy ,bg = "grey")
sell_btn = Button(window, text = "Sell", command=sell, bg ="grey")
#query_btn = Button(screen, text="Single Stock Query", command=create_window, bg="grey")
buy_btn.place(x = 15, y = 290)
sell_btn.place(x = 85, y = 290)
#query_btn.place(x=15, y=333)

window.mainloop()







transaction_1 = Transaction("Amazon","222","121","20","23/02/2023")
print(transaction_1.name)
print(transaction_1.id)
print(transaction_1.price)
print(transaction_1.amount)
print(transaction_1.date)

transaction_1.bought()
transaction_1.sold()

class Transaction:

  def __init__(self,name,id,price,amount,date):
    self.name = name
    self.id = id
    self.price = price
    self.amount = amount
    self.date = date
    
  def bought(self):
   
    #get entries from input box
    name = stockname.get().title()
    id = stockid.get()
    price = stockprice.get()
    amount = stockamount.get()
    date = stockdate.get()
    #delete entries after submit
    stockname.delete(0, END)
    stockid.delete(0, END)
    stockprice.delete(0, END)
    stockamount.delete(0, END)
    stockdate.delete(0, END)
    #save the entry in the file buy.csv
    file = open("buy.csv", "a", newline="")
    file.write(self.name + ";")
    file.write(self.id + ";")
    file.write(self.price + ";")
    file.write(self.amount + ";")
    file.write(self.date + "\n")

    print("This stock "+self.name+" is bought")
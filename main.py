from tkinter import *

def save():
  fn1 = firstname.get()
  ln1 = lastname.get()
  ag1 = age.get()
  print(fn1, ln1, ag1)
  firstname.delete(0, END)
  lastname.delete(0, END)
  age.delete(0, END)

#creating the file
  file = open("user.txt", "a")
  file.write(fn1)
  file.write(ln1)
  file.write(ag1)
  file.close()
  print("User", fn1, " has been registered successfully")


#screen design
screen = Tk()
screen.geometry("500x500")
screen.title("Redi Final Project")
heading = Label(text="Trading Performance Inquiry", bg="grey", fg="black", width="500")
heading.pack()

#label definition and position
firstname_text = Label(text = "Firstname *")
lastname_text = Label(text = "Lastname *")
age_text = Label(text = "Age *")
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)
age_text.place(x = 15, y = 210)

#firstname = StringVar()
#lastname = StringVar()
#age = IntVar()

#entry definition and position
firstname = Entry()
lastname = Entry()
age = Entry()
firstname.place(x = 15, y = 100)
lastname.place(x =15, y = 170)
age.place(x = 15, y = 240)

#place button to register
register = Button(screen, text = "Register", command = save, bg = "grey")
register.place(x =15, y = 290)

screen.mainloop()
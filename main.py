# imports
from tkinter import *
from tkinter import ttk
from random import *
from math import *
# stuff
# gui mostly generated using http://www.python-gui-builder.com/

# this is the function called when the button is clicked
strength = 1
def click():
  x =  money.get() + 1
  money.set(x)


# this is the function called when the button is clicked
def buy_clicker():
	if money.get() >= clicker_cost.get():
	  print('you can buy it')


# this is the function called when the button is clicked
def buy_strength():
	if money.get() >= strength_cost.get():
	  price = strength_cost.get()
	  print(price)
	 # new_price = round((0.4 * (10.0 ^ (1.4 * log(abs(price)))) - 15.0))
	 # print(new_price)
	  print(
	    round((0.1 * ((10.0 ** (1.1 * log(abs(price)))) - 15.0)))
	  )


root = Tk()
money = IntVar()
money.set(0)
clicker_cost = IntVar()
clicker_cost.set(25)
strength_cost = IntVar()
strength_cost.set(10)
# This is the section of code which creates the main window
root.geometry('1280x720')
root.configure(background='#F0F8FF')
root.title('Clicker Game')


# This is the section of code which creates a button
Button(root, text='Box that should be clicked', bg='#F0F8FF', font=('arial', 12, 'normal'), command=click).place(x=278, y=193)


# This is the section of code which creates the a label
Label(root, textvariable=str(money), bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=378, y=93)


# This is the section of code which creates a button
Button(root, text='buy a thing that clicks for you', bg='#F0F8FF', font=('arial', 12, 'normal'), command=buy_clicker).place(x=268, y=303)


# This is the section of code which creates a button
Button(root, text='increase how much you get for a click', bg='#F0F8FF', font=('arial', 12, 'normal'), command=buy_strength).place(x=248, y=343)


# This is the section of code which creates the a label
Label(root, text='cost', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=588, y=273)


# This is the section of code which creates the a label
Label(root, textvariable=str(clicker_cost), bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=588, y=313)


# This is the section of code which creates the a label
Label(root, textvariable=str(strength_cost), bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=588, y=343)


root.mainloop()

#--------------- Imports ---------------
from tkinter import * 
from random import *
from math import *

# this is the function called when the button is clicked

def click():
  money.set(money.get() + strength.get())

# this is the function called when the button is clicked
def auto_click():
    if money.get() >= clicker_cost.get():
        price = clicker_cost.get()
        money.set(money.get() - price)
        new_price = round(25 * 1.5)
        print(new_price)



# this is the function called when the button is clicked
def strength_upgrade():
    if money.get() >= strength_cost.get():
        price = strength_cost.get()
        money.set(money.get() - price)
        new_price = round(10 * 1.5)
        print(new_price)
        strength.set(strength.get() + 1)


root = Tk()
money = IntVar()
money.set(0)
clicker_cost = IntVar()
clicker_cost.set(25)
strength_cost = IntVar()
strength_cost.set(10)
strength = IntVar()
strength.set(1)
# This is the section of code which creates the main window
root.geometry('760x460')
root.configure(background='#F5F5DC')
root.title('Pringle')

Pringle = Canvas(root, height=256, width=256)
picture_file = PhotoImage(file = 'pringle.gif')
Pringle.create_image(128, 128, anchor=NE, image=picture_file)
Pringle.place(x=50, y=75)

#LABLE: Money counter
Label(root, textvariable=str(money), bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=135, y=20)

# clicky
Button(root, text='Click Here!', bg='#CDB79E', font=('helvetica', 24, 'bold'), command=click).place(x=100, y=360)


# auto clicker upgrade
Button(root, text='Auto clicker', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click).place(x=385, y=75)


# strength upgrade
Button(root, text='Click strength', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=strength_upgrade).place(x=385, y=158)


# upgrades
Label(root, text='Upgrades', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=415, y=20)


# cost
Label(root, text='Cost', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=675, y=20)


# autoclicker cost
Label(root, textvariable=str(clicker_cost), bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=695, y=78)


# strength cost
Label(root, textvariable=str(strength_cost), bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=695, y=178)


root.mainloop()

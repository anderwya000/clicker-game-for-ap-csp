#--------------- Imports ---------------
from tkinter import * 
from random import *
from math import *

# this is the function called when the button is clicked
strength = 1
def Click():
  print('clicked')
  x =  money.get() + strength
  money.set(x)

# this is the function called when the button is clicked
def auto_click():
	print('clicked')
	if money.get() >= clicker_cost.get():
		price = strength_cost.get()
		new_price = round((0.1 * ((10.0 ** (1.1 * log(abs(price)))) - 15.0)))

# this is the function called when the button is clicked
def upgrade():
	print('clicked')
	if money.get() >= strength_cost.get():
		price = strength_cost.get()
		new_price = round((0.1 * ((10.0 ** (1.1 * log(abs(price)))) - 15.0)))

# this is the function called when the button is clicked
def upgrade_2():
	print('clicked')

root = Tk()
money = IntVar()
money.set(0)
clicker_cost = IntVar()
clicker_cost.set(25)
strength_cost = IntVar()
strength_cost.set(10)
# This is the section of code which creates the main window
root.geometry('760x460')
root.configure(background='#F5F5DC')
root.title('Windows 11')


# First, we create a canvas to put the picture on
Pringle= Canvas(root, height=256, width=256)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
Pringle.create_image(256, 0, anchor=NE, image=picture_file)
Pringle.place(x=50, y=75)

#LABLE: Money counter
Label(root, text='12345', bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=135, y=20)

# This is the section of code which creates a button
Button(root, text='Click Here!', bg='#CDB79E', font=('helvetica', 24, 'bold'), command=Click).place(x=100, y=360)


# This is the section of code which creates a button
Button(root, text='Auto clicker', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click).place(x=385, y=75)


# This is the section of code which creates a button
Button(root, text='Clicker Upgrade 1', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=upgrade).place(x=385, y=158)


# This is the section of code which creates a button
Button(root, text='Clicker Upgrade 2', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=upgrade_2).place(x=385, y=248)


# This is the section of code which creates the a label
Label(root, text='Upgrades', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=415, y=20)


# This is the section of code which creates the a label
Label(root, text='Cost', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=675, y=20)


# This is the section of code which creates the a label
Label(root, text='10', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=695, y=78)


# This is the section of code which creates the a label
Label(root, text='25', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=695, y=178)


# This is the section of code which creates the a label
Label(root, text='100', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=685, y=268)


root.mainloop()


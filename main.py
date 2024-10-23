#--------------- Imports ---------------
from tkinter import * 
from random import *

# this is the function called when the button is clicked
strength = 1
def Click():
  print('clicked')
  x =  money.get() + strength
  money.set(x)

# this is the function called when the button is clicked
def auto_click():
	print('clicked')

# this is the function called when the button is clicked
def Upgrade():
	print('clicked')

# this is the function called when the button is clicked
def Upgrade():
	print('clicked')


root = Tk()

# This is the section of code which creates the main window
root.geometry('870x560')
root.configure(background='#F5F5DC')
root.title('Windows 11')


# First, we create a canvas to put the picture on
Pringle= Canvas(root, height=256, width=256)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
Pringle.create_image(256, 0, anchor=NE, image=picture_file)
Pringle.place(x=35, y=38)


# This is the section of code which creates a button
Button(root, text='Click Here!', bg='#CDB79E', font=('helvetica', 24, 'bold'), command=Click).place(x=55, y=318)


# This is the section of code which creates a button
Button(root, text='Auto clicker', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click).place(x=485, y=68)


# This is the section of code which creates a button
Button(root, text='Clicker Upgrade 1', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=Upgrade).place(x=485, y=158)


# This is the section of code which creates a button
Button(root, text='Clicker Upgrade 2', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=Upgrade).place(x=485, y=248)


# This is the section of code which creates the a label
Label(root, text='Upgrades', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=515, y=-2)


# This is the section of code which creates the a label
Label(root, text='Cost', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=775, y=-2)


# This is the section of code which creates the a label
Label(root, text='10', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=795, y=78)


# This is the section of code which creates the a label
Label(root, text='25', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=795, y=178)


# This is the section of code which creates the a label
Label(root, text='100', bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=785, y=268)


root.mainloop()


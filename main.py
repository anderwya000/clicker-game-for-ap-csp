# import
from tkinter import *

# this is the function called when the button is clicked
def run_clicks():
    money.set(money.get() + (strength.get() * clickers.get()))
    root.after(1000, run_clicks)

def calc_pringles():
    pringles_count.set(f'{money.get()} pringles')
    root.after(10, calc_pringles)

def click(event):
  money.set(money.get() + strength.get())

def auto_click_upgrade():
    if money.get() >= clicker_cost.get():
        price = clicker_cost.get()
        money.set(money.get() - price)
        new_price = round(price * 1.6)
        clicker_cost.set(new_price)
        clickers.set(clickers.get() + 1)



def strength_upgrade():
    if money.get() >= strength_cost.get():
        price = strength_cost.get()
        money.set(money.get() - price)
        new_price = round(price * 1.5)
        strength_cost.set(new_price)
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
clickers = IntVar()
clickers.set(0)
pringles_count = StringVar()
# This is the section of code which creates the main window
root.geometry('880x460')
root.configure(background='#F5F5DC')
root.title('Pringle')
run_clicks()
calc_pringles()

pringle = Canvas(root, height=256, width=256, bg='#F5F5DC', highlightthickness=0)
picture_file = PhotoImage(file = 'pringle.gif')
picture_file = picture_file.zoom(3, 3)
picture_file = picture_file.subsample(7, 7)
pringle.create_image(128, 128, image = picture_file)
pringle.place(x=50, y=75)
pringle.bind("<Button-1>", click)

# money

Label(root, textvariable = pringles_count, bg = '#F5F5DC', font = ('helvetica', 24, 'bold')).place(x = 50, y = 20)

# click it
Label(root, text='↑ Click it! ↑', bg = '#F5F5DC', font = ('helvetica', 24, 'bold')).place(x=90, y=360)


# upgrades
Label(root, text='Upgrades', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=415, y=60)


# auto clicker upgrade
Button(root, text='Auto clickers', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click_upgrade).place(x=385, y=115)


# strength upgrade
Button(root, text='Click strength', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=strength_upgrade).place(x=385, y=198)


# cost
Label(root, text='Cost', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=655, y=60)


# autoclicker cost
Label(root, textvariable=clicker_cost, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=655, y=115)


# strength cost
Label(root, textvariable=strength_cost, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=655, y=198)


# owned
Label(root, text='Amount', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=750, y=60)


# autoclicker owned
Label(root, textvariable=clickers, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=750, y=115)


# strength owned
Label(root, textvariable=strength, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=750, y=198)


root.mainloop()

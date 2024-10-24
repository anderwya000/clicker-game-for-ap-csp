"""https://github.com/anderwya000/clicker-game-for-ap-csp"""
# --------------- Imports ---------------
from tkinter import *
# --------------- Functions ---------------


def run_clicks():
    """Calculate the autoclicker gain."""
    money.set(money.get() + (strength.get() * clickers.get()))
    root.after(1000, run_clicks)


def calc_numbers():
    """Calculate the number to display as pringles."""
    if money.get() > 999999:
        pringles_count.set(f'{convert_to_e(money.get())} pringles')
    else:
        pringles_count.set(f'{money.get()} pringles')
    root.after(10, calc_numbers)


def click(event):
    """Click event handler. Gives more pringles."""
    money.set(money.get() + strength.get())


def auto_click_upgrade():
    """Check if the autoclicker upgrade is avaliable, then buy it."""
    if money.get() >= clicker_cost.get():
        price = clicker_cost.get()
        money.set(money.get() - price)
        new_price = round(price * 1.6)
        clicker_cost.set(new_price)
        clickers.set(clickers.get() + 1)


def strength_upgrade():
    """Check if the strength upgrade is avaliable, then buy it."""
    if money.get() >= strength_cost.get():
        price = strength_cost.get()
        money.set(money.get() - price)
        new_price = round(price * 1.6)
        strength_cost.set(new_price)
        strength.set(strength.get() + 1)


def convert_to_e(number):
    """Convert a number to scientific notation."""
    return '{:.2e}'.format(number)


root = Tk()

money = IntVar()
money.set(0)
clicker_cost = IntVar()
clicker_cost.set(10)
strength_cost = IntVar()
strength_cost.set(10)
strength = IntVar()
strength.set(1)
clickers = IntVar()
clickers.set(0)
pringles_count = StringVar()


root.geometry('880x460')
root.configure(background='#F5F5DC')
root.title('Pringle Clicker')

run_clicks()
calc_numbers()

pringle = Canvas(root, height=256, width=256, bg='#F5F5DC', highlightthickness=0)
picture_file = PhotoImage(file='pringle.gif')
picture_file = picture_file.zoom(3, 3)
picture_file = picture_file.subsample(7, 7)
pringle.create_image(128, 128, image=picture_file)
pringle.place(x=50, y=75)
pringle.bind("<Button-1>", click)

# --------------- User Interface ---------------

# LABEL: Money (pringles_count)
Label(root, textvariable=pringles_count, bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=50, y=20)

# LABEL: ↑ Click it! ↑
Label(root, text='↑ Click it! ↑', bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=90, y=360)

# LABELFRAME: upgrades area


# LABEL: Upgrades
Label(root, text='Upgrades', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=415, y=60)

# BUTTON: Auto Clickers Upgrade (auto_click_upgrade)
Button(root, text='Auto clickers', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click_upgrade).place(x=385, y=115)

# BUTTON: Click Strength Upgrade (strength_upgrade)
Button(root, text='Click strength', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=strength_upgrade).place(x=385, y=198)

# LABEL: Cost
Label(root, text='Cost', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=600, y=60)

# LABEL: Autoclicker Cost (clicker_cost)
Label(root, textvariable=clicker_cost, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=600, y=115)

# LABEL: Strength Cost (strength_cost)
Label(root, textvariable=strength_cost, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=600, y=198)

# LABEL: Amount Owned
Label(root, text='Amount', bg='#F5F5DC', font=('helvetica', 22, 'bold')).place(x=750, y=60)

# LABEL: Clickers Owned (clickers)
Label(root, textvariable=clickers, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=750, y=115)

# LABEL: Click Strength (strength)
Label(root, textvariable=strength, bg='#F5F5DC', font=('helvetica', 20, 'bold')).place(x=750, y=198)

# --------------- End ---------------
root.mainloop()

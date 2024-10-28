"""https://github.com/anderwya000/clicker-game-for-ap-csp"""
# --------------- Imports ---------------
from tkinter import *
from random import randrange
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
    global color_index
    money.set(money.get() + strength.get())
    if randrange(0,1001) == 1000:
        color_index += 1
        if color_index > 3:
            color_index = 0
        pringle.itemconfig(normal_pringle, state='hidden')
        pringle.itemconfig(green_pringle, state='hidden')
        pringle.itemconfig(blue_pringle, state='hidden')
        pringle.itemconfig(red_pringle, state='hidden')
        pringle.itemconfig(pringle_colors[color_index], state='normal')
        # money.set(money.get() + (1000 * strength.get()))



def auto_click_upgrade():
    """Check if the autoclicker upgrade is available, then buy it."""
    if money.get() >= clicker_cost.get():
        price = clicker_cost.get()
        money.set(money.get() - price)
        new_price = round(price * 1.6)
        clicker_cost.set(new_price)
        clickers.set(clickers.get() + 1)


def strength_upgrade():
    """Check if the strength upgrade is available, then buy it."""
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
color_index = 0

root.geometry('880x460')
root.configure(background='#F5F5DC')
root.title('Pringle Clicker')

run_clicks()
calc_numbers()

pringle = Canvas(root, height=256, width=256, bg='#F5F5DC', highlightthickness=0)
picture_file1 = PhotoImage(file='normal_pringle.gif')
picture_file1 = picture_file1.zoom(3)
picture_file1 = picture_file1.subsample(7)
normal_pringle = pringle.create_image(128, 128, image=picture_file1)
pringle.itemconfig(normal_pringle, state='normal')

picture_file2 = PhotoImage(file='green_pringle.gif')
picture_file2 = picture_file2.zoom(3)
picture_file2 = picture_file2.subsample(7)
green_pringle = pringle.create_image(128, 128, image=picture_file2)
pringle.itemconfig(green_pringle, state='hidden')

picture_file3 = PhotoImage(file='blue_pringle.gif')
picture_file3 = picture_file3.zoom(3)
picture_file3 = picture_file3.subsample(7)
blue_pringle = pringle.create_image(128, 128, image=picture_file3)
pringle.itemconfig(blue_pringle, state='hidden')

picture_file4 = PhotoImage(file='red_pringle.gif')
picture_file4 = picture_file4.zoom(3)
picture_file4 = picture_file4.subsample(7)
red_pringle = pringle.create_image(128, 128, image=picture_file4)
pringle.itemconfig(red_pringle, state='hidden')

pringle_colors = [normal_pringle, green_pringle, blue_pringle, red_pringle]
pringle.place(x=50, y=75)
pringle.bind("<Button-1>", click)

# --------------- User Interface ---------------

# LABEL: Money (pringles_count)
Label(root, textvariable=pringles_count, bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=100, y=20)

# LABEL: ↑ Click it! ↑
Label(root, text='↑ Click it! ↑', bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=90, y=360)

# FRAME: Upgrades
upgrade_frame = Frame(root, bg='#CF9E54', bd=5, relief=SUNKEN)
upgrade_frame.place(x=350, y=110)
upgrade_frame.columnconfigure(0, weight=3)
upgrade_frame.columnconfigure(1, weight=3)
upgrade_frame.columnconfigure(2, weight=1)
upgrade_frame.rowconfigure(0, weight=1)
upgrade_frame.rowconfigure(1, weight=1)
upgrade_frame.rowconfigure(2, weight=1)

# LABEL: Upgrades
Label(upgrade_frame, text='Upgrades', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=0, row=0, padx=10, pady=10)

# BUTTON: Auto Clickers Upgrade (auto_click_upgrade)
Button(upgrade_frame, text='Auto clickers', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click_upgrade).grid(column=0, row=1, padx=10, pady=10)

# BUTTON: Click Strength Upgrade (strength_upgrade)
Button(upgrade_frame, text='Click strength', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=strength_upgrade).grid(column=0, row=2, padx=10, pady=10)

# LABEL: Cost
Label(upgrade_frame, text='Cost', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=1, row=0, padx=10, pady=10)

# LABEL: Autoclicker Cost (clicker_cost)
Label(upgrade_frame, textvariable=clicker_cost, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=1, row=1, padx=10, pady=10)

# LABEL: Strength Cost (strength_cost)
Label(upgrade_frame, textvariable=strength_cost, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=1, row=2, padx=10, pady=10)

# LABEL: Amount Owned
Label(upgrade_frame, text='Amount', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=2, row=0, padx=10, pady=10)

# LABEL: Clickers Owned (clickers)
Label(upgrade_frame, textvariable=clickers, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=2, row=1, padx=10, pady=10)

# LABEL: Click Strength (strength)
Label(upgrade_frame, textvariable=strength, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=2, row=2, padx=10, pady=10)

# --------------- End ---------------
root.mainloop()

"""https://github.com/anderwya000/clicker-game-for-ap-csp"""
# --------------- Imports ---------------
# ---------- Luke ----------
from tkinter import *
import turtle
from random import randrange


# --------------- Functions ---------------

# ----------- Wyatt ----------
def run_clicks():
    """Calculate the autoclicker gain."""
    money.set(money.get() + (strength.get() * clickers.get()))
    root.after(1000, run_clicks)


def calc_numbers():
    """Calculate the number to display as pringles."""
    if money.get() > 999999: # Converts to sci notation when money count reaches 1 Million
        pringles_count.set(f'{convert_to_e(money.get())} pringles')
    else:
        pringles_count.set(f'{money.get()} pringles')
    root.after(10, calc_numbers)


def convert_to_e(number):
    """Convert a number to scientific notation."""
    return '{:.2e}'.format(number)


def click(event):
    """Click event handler. Gives more pringles."""
    money.set(money.get() + strength.get())
    # Creates a 0.4% chance that the Pringle will cycle one through the list of colors upon a click
    global color_index
    if randrange(0,251) == 250:
        color_index += 1
        if color_index > 3:
            color_index = 0
        # Hides all pringles and shows the new color
        pringle.itemconfig(normal_pringle, state='hidden')
        pringle.itemconfig(green_pringle, state='hidden')
        pringle.itemconfig(blue_pringle, state='hidden')
        pringle.itemconfig(red_pringle, state='hidden')
        pringle.itemconfig(pringle_colors[color_index], state='normal') # Shows the appropriate colored pringle from the list
        money.set(money.get() + (strength.get() * 100)) # Gives 100x extra pringles upon a color change

# ---------- Luke ----------
def click_julius(event):
   """Julius' click event handler. Gives more Pringles"""
   # Gets the position relative to the canvas
   x_click = event.x
   y_click = event.y
   # Converts canvas click coordinates to turtle screen coordinates
   turtle_canvas_width = turtle_canvas.winfo_width()
   turtle_canvas_height = turtle_canvas.winfo_height()
   # Adjusts click position to match Turtle screen coordinates
   x_click_turtle = x_click - turtle_canvas_width / 2  # Center the x-coordinate
   y_click_turtle = (turtle_canvas_height / 2) - y_click  # Flip y-coordinate
   # Gets Julius' position
   julius_x = Julius.xcor()
   julius_y = Julius.ycor()
   # Gets the boundary box for Julius
   julius_left = julius_x - click_radius
   julius_right = julius_x + click_radius
   julius_top = julius_y + click_radius
   julius_bottom = julius_y - click_radius
   # Checks if the click is inside the bounding box of Julius
   if julius_left <= x_click_turtle <= julius_right and julius_bottom <= y_click_turtle <= julius_top:
     print("HIT")
     money.set(money.get() + (strength.get() * 10)) # Gives 10x the money that the big pringle does


def auto_click_upgrade():
   """Check if the autoclicker upgrade is available, then buy it."""
   if money.get() >= clicker_cost.get():
     # Gets the price of the auto clicker and subtracts it from the total money
     price = clicker_cost.get()
     money.set(money.get() - price)
     # Multiplies the price of auto clicker by 1.6x
     new_price = round(price * 1.6)
     clicker_cost.set(new_price)
     # Gives 1 auto clicker
     clickers.set(clickers.get() + 1)


def strength_upgrade():
   """Check if the strength upgrade is available, then buy it."""
   if money.get() >= strength_cost.get():
     # Gets the price of the strength and subtracts it from the total money
     price = strength_cost.get()
     money.set(money.get() - price)
     # Multiplies the price of auto clicker by 1.6x
     new_price = round(price * 1.6)
     strength_cost.set(new_price)
     # Gives 1 more strength
     strength.set(strength.get() + 1)


# --------------- Variables ---------------

# ---------- Wyatt ----------
root = Tk() # Creates the main tkinter window for display
# Declare tkinter variables for display
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
# Turtle variables
turn = 0
margin = 25 # Sets the distance between the canvas edge and Julius
click_radius = 40  # Sets the click radius around Julius


# ---------- Luke ----------

# Cofiguration for the Tkinter canvas
root.geometry('880x660')
root.configure(background='#F5F5DC')
root.title('Pringle Clicker')

# Starts looping functions.
run_clicks()
calc_numbers()


# -------------- Turtles --------------

# --------- Luke ----------
# Initialize Turtle Screen
turtle_canvas = Canvas(root, width=880, height=660, bg='#F5F5DC',)
turtle_canvas.place(x=0, y=0)  # Place the canvas inside the window

# Creates the Turtle screen and binds it to the Tkinter canvas
turtle_screen = turtle.TurtleScreen(turtle_canvas)
turtle_screen.bgcolor("#F5F5DC")  # Matches the background color of the Tkinter window

# Initialize Turtle (Julius)
Julius = turtle.RawTurtle(turtle_screen)
Julius.ht()
Julius.speed(0)
Julius.penup()
Julius.goto(margin - turtle_canvas.winfo_width() / 2, -(margin - turtle_canvas.winfo_height() / 2)) # Formats turtle start to fit tkinter canvas coords

# Sets Up Julius' image
image_file = 'Mr.Julius_Pringle.gif'
# Checks if the image exists before adding it
try:
   turtle_screen.addshape(image_file)  # Register the .gif shape
except Exception as e:
   print(f"Error registering the image as a shape: {e}")
# Sets the shape of the RawTurtle to the registered image
Julius.shape(image_file)

Julius.st()

turtle_canvas.bind("<Button-1>", click_julius) # Binds the click_Julius to Julius


# --------------- Picture File Set Ups ---------------

# ---------- Luke ----------
# Set up pringle image
pringle = Canvas(root, height=256, width=256, bg='#F5F5DC', highlightthickness=0)
picture_file1 = PhotoImage(file='normal_pringle.gif')
picture_file1 = picture_file1.zoom(3)
picture_file1 = picture_file1.subsample(7)
normal_pringle = pringle.create_image(128, 128, image=picture_file1)
pringle.itemconfig(normal_pringle, state='normal')
# ---------- Wyatt ----------
# Create the green pringle picture and hide it to start
picture_file2 = PhotoImage(file='green_pringle.gif')
picture_file2 = picture_file2.zoom(3)
picture_file2 = picture_file2.subsample(7)
green_pringle = pringle.create_image(128, 128, image=picture_file2)
pringle.itemconfig(green_pringle, state='hidden')
# Create the blue pringle picture and hide it to start
picture_file3 = PhotoImage(file='blue_pringle.gif')
picture_file3 = picture_file3.zoom(3)
picture_file3 = picture_file3.subsample(7)
blue_pringle = pringle.create_image(128, 128, image=picture_file3)
pringle.itemconfig(blue_pringle, state='hidden')
# Create the red pringle picture and hide it to start
picture_file4 = PhotoImage(file='red_pringle.gif')
picture_file4 = picture_file4.zoom(3)
picture_file4 = picture_file4.subsample(7)
red_pringle = pringle.create_image(128, 128, image=picture_file4)
pringle.itemconfig(red_pringle, state='hidden')
# ---------- Wyatt ----------
pringle_colors = [normal_pringle, green_pringle, blue_pringle, red_pringle] # Creates the pringles list of colors
pringle.place(x=50, y=130) # Places the pringle on the screen
pringle.bind("<Button-1>", click) # Binds the pringle to the click function


# --------------- User Interface ---------------

# ---------- Luke ----------
# LABEL: Money (pringles_count)
Label(root, textvariable=pringles_count, bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=100, y=80)

# LABEL: ↑ Click it! ↑
Label(root, text='↑ Click it! ↑', bg='#F5F5DC', font=('helvetica', 24, 'bold')).place(x=90, y=420)
# ---------- Wyatt ----------
# FRAME: Upgrades
# Configure the frame that the upgrades are in. 
upgrade_frame = Frame(root, bg='#CF9E54', bd=5, relief=SUNKEN)
upgrade_frame.place(x=350, y=170)
upgrade_frame.columnconfigure(0, weight=3)
upgrade_frame.columnconfigure(1, weight=3)
upgrade_frame.columnconfigure(2, weight=1)
upgrade_frame.rowconfigure(0, weight=1)
upgrade_frame.rowconfigure(1, weight=1)
upgrade_frame.rowconfigure(2, weight=1)

# ---------- Luke ----------
# LABEL: Upgrades
Label(upgrade_frame, text='Upgrades', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=0, row=0, padx=10, pady=10)

# BUTTON: Auto Clickers Upgrade (auto_click_upgrade)
Button(upgrade_frame, text='Auto clickers', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=auto_click_upgrade).grid(column=0, row=1, padx=10, pady=10)

# BUTTON: Click Strength Upgrade (strength_upgrade)
Button(upgrade_frame, text='Click strength', bg='#CDB79E', font=('helvetica', 20, 'bold'), command=strength_upgrade).grid(column=0, row=2, padx=10, pady=10)

# LABEL: Cost
Label(upgrade_frame, text='Cost', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=1, row=0, padx=10, pady=10)
# ---------- Wyatt, Luke ----------
# LABEL: Autoclicker Cost (clicker_cost)
Label(upgrade_frame, textvariable=clicker_cost, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=1, row=1, padx=10, pady=10)

# LABEL: Strength Cost (strength_cost)
Label(upgrade_frame, textvariable=strength_cost, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=1, row=2, padx=10, pady=10)
# ---------- Luke ----------
# LABEL: Amount Owned
Label(upgrade_frame, text='Amount', bg='#CF9E54', font=('helvetica', 22, 'bold')).grid(column=2, row=0, padx=10, pady=10)

# LABEL: Clickers Owned (clickers)
Label(upgrade_frame, textvariable=clickers, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=2, row=1, padx=10, pady=10)

# LABEL: Click Strength (strength)
Label(upgrade_frame, textvariable=strength, bg='#CF9E54', font=('helvetica', 20, 'bold')).grid(column=2, row=2, padx=10, pady=10)


# --------------- Julius movement -------------

# ---------- Luke ----------
# Start to move Julius around the screen
while True:
   Julius.forward(3)
   # Check if the turtle hits the right boundary if it does, turn right
   if (Julius.xcor() > (370 - margin)):
     if (turn == 0): # Sets turn back to zero 
       Julius.back(margin)
       Julius.right(90)
   elif (Julius.ycor() < (margin - 280)):
     if (turn == 0):
       Julius.back(margin)
       Julius.right(90)
       turn = 1  # Sets turn to 1 after turning to ensure that Julius doesn't pass multiple boundary checks early
   elif (Julius.xcor() < (margin - 460)):
     if (turn == 1):
       Julius.back(margin)
       Julius.right(90)
   elif (Julius.ycor() > (355 - margin)):
     if (turn == 1):
       Julius.back(margin)
       Julius.right(90)
       turn = 0  # Set turn back to 0


# --------------- End ---------------
root.mainloop()


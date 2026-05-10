from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
import random
BACKGROUND_COLOR = "#B1DDC6"



# ----------------------------- SETUP GUI --------------------------------------------------------

#Window
window = Tk()
window.geometry("500x500")
window.configure(background=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=400, height=400)
canvas.pack()


#Buttons
RIGHT_BUTTON = PhotoImage(file="./images/right.png")
WRONG_BUTTON = PhotoImage(file="./images/wrong.png")
button_x = Button(image=RIGHT_BUTTON, highlightthickness=0)
button_y = Button(image=WRONG_BUTTON, highlightthickness=0)













window.mainloop()


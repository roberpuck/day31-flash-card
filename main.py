
from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD_COLOR = '#91C2AF'

try:
    data = pd.read_csv('./data/spanish_words.csv')
except FileNotFoundError:
    print('File not found')
finally:
    data_dict = data.to_dict()

known_words =[]
words_to_learn = []


# ----------------------------- Buttons Functionality --------------------------------------------------------

def press_x():
    global word_index,spanish_word,english_word
    reset_screen()
    words_to_learn.append(spanish_word)
    word_index = pick_card()
    spanish_word = data_dict['Spanish'][word_index]
    english_word = data_dict['English'][word_index]
    update_spanish_card()
    return

def press_y():
    global word_index,spanish_word,english_word,data_dict
    reset_screen()
    known_words.append(spanish_word)
    del data_dict['Spanish'][word_index]
    del data_dict['English'][word_index]
    word_index = pick_card()
    spanish_word = data_dict['Spanish'][word_index]
    english_word = data_dict['English'][word_index]
    update_spanish_card()
    # timer()
    return


# ----------------------------- Change Flash Card --------------------------------------------------------
def change_card():
    global card_image_back,language_label,word_label
    canvas.create_image(400, 268, image=card_image_back)
    language_label.configure(text=language[1], fg='white', bg=BACK_CARD_COLOR)
    word_label.configure(text=english_word, fg='white', bg=BACK_CARD_COLOR)

def pick_card():
    global data_dict
    if data_dict['Spanish']:
        data_dict_keys = list(data_dict['Spanish'].keys())
        card = random.choice(data_dict_keys)
        print(f'The card is {card}')
        return card
    else:
        print(data_dict['Spanish'])
        messagebox.showinfo(title='All the words learnt',message='Congrats! you learnt the most common words!')

def update_spanish_card():
    global word_label,language_label,card_image_front
    canvas.itemconfig(canvas_card, image=card_image_front)
    word_label.config(text=spanish_word,bg='white')
    language_label.config(text=language[0],bg='white')
    window.after(3000,update_english_card)


def update_english_card():
    global word_label, language_label,card_image_back
    word_label.config(text=english_word,bg=BACK_CARD_COLOR)
    language_label.config(text=language[1],bg=BACK_CARD_COLOR)
    canvas.itemconfig(canvas_card,image=card_image_back)

def reset_screen():
    word_label.configure(text='')
    language_label.configure(text='')

# ----------------------------- SETUP GUI --------------------------------------------------------

#Window
window = Tk()

window.configure(background=BACKGROUND_COLOR,pady=50,padx=50,width=800,height=526)

#Canvas
card_image_front = PhotoImage(file='./images/card_front.png')
card_image_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=526,highlightthickness=0,background=BACKGROUND_COLOR)
canvas_card = canvas.create_image(400,268,image=card_image_front)
canvas.grid(column=0,row=0,columnspan=2)

# Labels
word_index = pick_card()
language = ['Spanish', 'English']
spanish_word = data_dict['Spanish'][word_index]
english_word = data_dict['English'][word_index]
language_label = Label(text=language[0], font=('Arial', 40, 'italic'), highlightthickness=0,background='white')
word_label = Label(text=spanish_word, font=('Arial', 60, 'bold'), highlightthickness=0,background='white')
language_label.place(x=300, y=150)
word_label.place(x=300, y=263)

# Buttons
RIGHT_BUTTON = PhotoImage(file="./images/right.png")
WRONG_BUTTON = PhotoImage(file="./images/wrong.png")
button_y = Button(image=RIGHT_BUTTON, highlightthickness=0, background=BACKGROUND_COLOR, command=press_y)
button_x = Button(image=WRONG_BUTTON, highlightthickness=0, background=BACKGROUND_COLOR, command=press_x)
button_x.grid(column=0, row=1)
button_y.grid(column=1, row=1)

window.mainloop()


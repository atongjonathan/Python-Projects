from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
english_word = ''
window = Tk()
window.title("Flash app")
known = []
window.config(height=700, width=800, pady=50, padx=50, bg=BACKGROUND_COLOR)
# Images
right = PhotoImage(file="../flash-card/images/right.png")
wrong = PhotoImage(file="../flash-card/images/wrong.png")
card_front = PhotoImage(file="../flash-card/images/card_front.png")
card_back = PhotoImage(file="../flash-card/images/card_back.png")
start = PhotoImage(file="../flash-card/images/start.png")

# Data
data = pd.read_csv("../flash-card/data/french_words.csv")


def generate_words():
    card.create_image(320, 200, image=card_back)
    card.create_text(350, 100, text="English", fill="white", font=("Arial", 20, "italic"))
    card.create_text(350, 200, text=f"{english_word}", fill="white", font=("Arial", 35, "bold"))


def change_card():
    french_word = random.choice(data.French)
    fre_list = data.French.to_list()
    index = fre_list.index(french_word)
    global english_word
    english_word = data.English[index]
    card.create_image(320, 200, image=card_front)
    card.create_text(350, 100, text="French", font=("Arial", 20, "italic"))
    card.create_text(350, 200, text=f"{french_word}", font=("Arial", 35, "bold"))
    window.after(3500, generate_words)


# UI
card = Canvas(height=350, width=700, highlightthickness=0)
card.create_image(320, 200, image=card_back)
card.create_text(350, 100, text="Welcome \nTo\n Flash Card", fill="white", font=("Arial", 30, "bold"))

card.grid(row=1, column=1, columnspan=3)

right_button = Button(image=right, command=change_card, highlightthickness=0,)
right_button.config(highlightthickness=0)
right_button.grid(column=3, row=2)

wrong_button = Button(image=wrong, command=change_card, highlightthickness=0)
wrong_button.grid(column=1, row=2)

start_button = Button(image=start, command=change_card,  highlightthickness=0)
start_button.grid(column=2, row=2)

window.mainloop()

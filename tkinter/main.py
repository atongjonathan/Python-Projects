from tkinter import *


def button_clicked():
    my_label.config(text="Some Text")


window = Tk()
window.minsize(width=500, height=300)
window.title("My first GUI program")
window.config(padx=100, pady=100)
# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="Configured_text", padx=50, pady=50)
# my_label.pack()  # To show it on screen
# my_label.place(x=100, y=200)
my_label.grid(column=1, row=1)  # Only one between pack, grid and place
# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=1)
# Entry
entry = Entry(width=10)
print(entry.get())
entry.grid(column=4, row=3)

window.mainloop()

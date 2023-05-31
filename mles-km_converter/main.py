from tkinter import *


def calculate_km():
    result = float(entry.get()) * 1.689
    answer.config(text=result)


window = Tk()
window.minsize(width=300, height=100)
window.title("My miles to km converter")
window.config(pady=20, padx=20)

entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(column=2, row=1)

miles = Label(text="Miles", font=("Arial", 12, 'bold'))
miles.grid(column=3, row=1)

equal_label = Label(text="is equal to", font=("Arial", 12, 'bold'))
equal_label.grid(column=1, row=2)

answer = Label(text="0", font=("Arial", 12, 'bold'))
answer.grid(column=2, row=2)
km = Label(text="Km", font=("Arial", 12, 'bold'))
km.grid(column=3, row=2)

button = Button(text="Calculate", command=calculate_km, font=("Arial", 12, 'bold'))
button.grid(column=2, row=3)

window.mainloop()

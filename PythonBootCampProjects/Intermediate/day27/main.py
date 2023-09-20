from tkinter import *


def miles_converter():
    value = float(input.get())
    converter = value * 1.6
    result = Label(window, text = converter).grid(row = 1, column = 1)
    return
    

window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=200, height=100)

#Labels
input = StringVar()
miles_input = Entry(window, textvariable = input, width=5).grid(row = 0, column = 1)

my_label_text = Label(text = "is equal to ", font=("Arial", 10, "bold")).grid(column=0, row=1)

my_label_miles = Label(window, text = 'miles', font=("Arial", 10, "bold")).grid(column=2, row=0)

my_label_km = Label(text = "Km", font=("Arial", 10, "bold")).grid(column=2, row=1)

my_label_0 = Label(text = "0", font=("Arial", 10, "bold")).grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=miles_converter)
button.grid(column=1, row=2)


window.mainloop()
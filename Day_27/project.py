from tkinter import *


def button_clicked():
    miles_to_km = round(int(input_miles.get()) / 0.62137, 2)
    num_km_label.config(text=miles_to_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=100)

# Entry
input_miles = Entry(width=10, justify="center")
input_miles.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label variable
num_km_label = Label(text="0")
num_km_label.grid(column=1, row=1)
num_km_label.config(padx=10, pady=20)

# Label
km_my_label = Label(text="Km")
km_my_label.grid(column=2, row=1)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)


















window.mainloop()
from tkinter import *


def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles / 0.62137, 2)
    num_km_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
input_miles = Entry(width=10, justify="center")
input_miles.grid(column=1, row=0)

# Label 'Miles'
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label convert result
num_km_label = Label(text="0")
num_km_label.grid(column=1, row=1)
num_km_label.config(padx=10, pady=20)

# Label 'Km'
km_result_label = Label(text="Km")
km_result_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


















window.mainloop()
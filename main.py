from tkinter import *

FONT = ("Arial", 14, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
window.minsize(width=200, height=200)

input_miles = Entry(width=10)
input_miles.grid(column=2, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

conversion_label = Label(text="0", font=FONT)
conversion_label.grid(column=2, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=3, row=1)


def calculate_km():
    miles = float(input_miles.get())
    kilometers = miles * 1.60934
    conversion_label.config(text=f"{kilometers}")


calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=2, row=2)


window.mainloop()

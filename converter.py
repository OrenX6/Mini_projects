from tkinter import *

FONT = ("Comic Sans MS", 14, "bold")


def miles_to_km():
    miles = float(text_box.get())
    km = round(miles * 1.609344, 2)
    result_label.config(text=f"{km}")


def km_to_miles():
    km = float(text_box.get())
    miles = round(km * 0.62137119, 2)
    result_label.config(text=f"{miles}")


def convert():
    choice = listbox.selection_get()  # string
    if choice == "Miles To Kilometer":
        miles_to_km()
    else:
        km_to_miles()


def on_selection(event):
    choice = listbox.selection_get()
    if choice == "Miles To Kilometer":
        miles_label.grid(row=0, column=2)
        km_label.grid(row=1, column=2)

    else:
        miles_label.grid(row=1, column=2)
        km_label.grid(row=0, column=2)

    text_box.delete(0, END)
    result_label.config(text="0")


master = Tk()
master.wm_title("Convertor")
master.config(padx=30, pady=30)

# Labels
equal_label = Label(master, text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

miles_label = Label(master, text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

result_label = Label(master, text=0, font=FONT)
result_label.config(padx=10, pady=10)
result_label.grid(row=1, column=1)

km_label = Label(master, text="Km", font=FONT)
km_label.grid(row=1, column=2)

mode_label = Label(master, text="Select Mode:", font=FONT)
mode_label.grid(row=0, column=3)

# Button
button = Button(master, text="Calculate", font=FONT, fg="blue", command=convert)
button.grid(row=2, column=1)

# Entry
text_box = Entry(master, width=8, font=FONT, justify="center", fg="green")
text_box.grid(row=0, column=1)

# Listbox
listbox = Listbox(master, height=2, font=FONT, justify="center", activestyle="none")
# Add two elements to the end of the list.
listbox.insert(END, "Miles To Kilometer", "Kilometer To Miles")  # Index tk.END refers to the last line in the listbox.

listbox.grid(row=1, column=3)
listbox.bind("<<ListboxSelect>>", func=on_selection)
listbox.select_set(0)
master.mainloop()

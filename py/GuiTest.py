import tkinter as tk
import datetime

def set_date():
    selected_date = date_entry.get()
    try:
        selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d')
        display_label.config(text=selected_date.strftime('%B %d, %Y'))
    except ValueError:
        display_label.config(text='Invalid date format')

root = tk.Tk()
root.title("Date Selector")

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

date_label = tk.Label(root, text="Enter a date (YYYY-MM-DD):")
date_entry = tk.Entry(root)
date_entry.insert(0, current_date)
display_label = tk.Label(root, text=current_date)

set_button = tk.Button(root, text="Set", command=set_date)

date_label.pack()
date_entry.pack()
display_label.pack()
set_button.pack()

root.mainloop()
"""
Caleb Aguiar
SWE-410
02/04/2025
TKinter Example
In Class Exercise
"""
# Import all classes and methods from the tkinter module
from tkinter import *

# Create the main application window
tk = Tk()

# Use grid for consistency 
# Create a label for displaying a title or message 
header_label = Label(tk,text="SWE-410 Tkinter Example",width=50, height=5)

# Place the label in row 0, spanning 2 columns to center it 
header_label.grid(row=0, column=0, columnspan=2)

# Create a label for First Name and place it in row 1 column 0
Label(tk, text="First Name").grid(row=1,column=0)
Label(tk, text="Last Name").grid(row=2,column=0)

# Create a Entry widget (text input field) for first name
first_name_entry = Entry(tk)
last_name_entry = Entry(tk)

# Place the first Entry Widget in row 1, col 1
first_name_entry.grid(row=1,column=1)
last_name_entry.grid(row=2,column=1)

# Create a button labeled Stop
button = Button(tk, text="Stop",width=25, command=tk.destroy)

# Place the button in row 3, span 2 columns 
button.grid(row=3, column=0, columnspan=2)

# Run the TKinter event loop to keep the application window open 
tk.mainloop()
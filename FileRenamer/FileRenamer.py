import os
from tkinter import Tk, Label, Entry, Button, Listbox, filedialog, END, messagebox

def select_files():
    global files
    files = filedialog.askopenfilenames(title="Select Files")
    listbox.delete(0, END)  # Clear the listbox
    for file in files:
        listbox.insert(END, os.path.basename(file))

def preview_rename():
    base_name = entry.get()
    if not base_name:
        messagebox.showwarning("Input Error", "Please enter a base name.")
        return

    listbox.delete(0, END)
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name} {i}{os.path.splitext(file)[1]}"
        listbox.insert(END, new_name)

def rename_files():
    base_name = entry.get()
    if not base_name:
        messagebox.showwarning("Input Error", "Please enter a base name.")
        return

    for i, file in enumerate(files, start=1):
        directory = os.path.dirname(file)
        extension = os.path.splitext(file)[1]
        new_name = f"{base_name} {i}{extension}"
        new_path = os.path.join(directory, new_name)
        os.rename(file, new_path)

    messagebox.showinfo("Success", "Files renamed successfully!")
    listbox.delete(0, END)

# GUI setup
root = Tk()
root.title("File Renamer")

# Base name input
Label(root, text="Enter Base Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry = Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

# Buttons
Button(root, text="Select Files", command=select_files).grid(row=1, column=0, padx=10, pady=10)
Button(root, text="Preview Rename", command=preview_rename).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Rename Files", command=rename_files).grid(row=1, column=2, padx=10, pady=10)

# Listbox for preview
listbox = Listbox(root, width=50, height=15)
listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

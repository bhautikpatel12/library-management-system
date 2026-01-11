
# library_gui.py
import tkinter as tk
from tkinter import messagebox

books = {}

def add_book():
    books[bid.get()] = {
        "name": name.get(),
        "author": author.get(),
        "qty": int(qty.get())
    }
    messagebox.showinfo("Success", "Book Added")

def view_books():
    output.delete("1.0", tk.END)
    for b in books:
        output.insert(tk.END, f"{b} : {books[b]}\n")

root = tk.Tk()
root.title("Library Management System")

tk.Label(root, text="Book ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Author").grid(row=2, column=0)
tk.Label(root, text="Quantity").grid(row=3, column=0)

bid = tk.Entry(root)
name = tk.Entry(root)
author = tk.Entry(root)
qty = tk.Entry(root)

bid.grid(row=0, column=1)
name.grid(row=1, column=1)
author.grid(row=2, column=1)
qty.grid(row=3, column=1)

tk.Button(root, text="Add Book", command=add_book).grid(row=4, column=0)
tk.Button(root, text="View Books", command=view_books).grid(row=4, column=1)

output = tk.Text(root, height=10, width=40)
output.grid(row=5, column=0, columnspan=2)

root.mainloop()

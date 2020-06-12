import tkinter as tk
from tkinter import ttk


def addition():
    x = num_one.get()
    y = num_two.get()
    ans = x + y
    lblAnswer.config(text=str(ans))

root = tk.Tk()

num_one = tk.DoubleVar()
num_two = tk.DoubleVar()

entNum_one = ttk.Entry(root, textvariable=num_one)
entNum_one.pack()

entNum_two = ttk.Entry(root, textvariable=num_two)
entNum_two.pack()

lblAnswer = ttk.Label(root, text="this is a label", padding=(10, 10))
lblAnswer.pack()

btnGetanswer = ttk.Button(root, text="add", command=addition)
btnGetanswer.pack()

root.mainloop()
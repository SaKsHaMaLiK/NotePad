import tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk
from datetime import datetime
import webbrowser

root = tk.Tk()
root.geometry('500x500')
root.title('notepad')
root.iconbitmap('notepad.ico')


menubar = Menu(root)

file = Menu(meubar, tearoff=0)
file.add_command(label="New", command=new)
file.add_command(label="Newwindow", command=new_window)
file.add_command(label="Open", command=Open)
file.add_command(label="Save", command=save)
file.add_command(label="SaveAs", command=save_as)
file.add_separator()
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label="file", menu=file, font=('verdana', 10, 'bold'))

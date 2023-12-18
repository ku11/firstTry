import tkinter as tk
from tkinter import *
from tkinter import filedialog
from client import *
from PIL import Image, ImageTk


class MyWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1300x500")
        self.panel = Label()
        self.resizable(width=False, height=False)
        self.title("Watermarking an image")
        self.btn1 = Button(text="Выбрать картинку", background="grey", foreground="black",
                           padx="180", pady="7", font="13", command=self.open_img)
        self.btn1.place(x=50, y=20)
        self.btn2 = Button(text="Нанести водяной знак", background="grey", foreground="black",
                           padx="162", pady="7", font="13", command=self.send_image)
        self.btn2.place(x=50, y=80)
        self.box = Listbox(width=90, height=20)
        self.box.place(x=50, y=150)
        self.send_path = ''


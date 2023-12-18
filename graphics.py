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

    # Открыть картинку
    def open_img(self):
        try:
            if self.send_path != '':
                self.clear_label_image()
            self.box.delete(0, END)
            path = filedialog.askopenfilename(title='Открыть', type=".jpg")
            if path:
                self.send_path = path
                img = ImageTk.PhotoImage(Image.open(path).resize((650, 400)))
                self.panel = Label(image=img)
                self.panel.image = img
                self.panel.place(x=620, y=40)
            else:
                self.send_path = ''
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def clear_label_image(self):
        self.panel.destroy()

    def display(self, image):
        try:
            self.clear_label_image()
            self.panel = Label(image=image)
            self.panel.image = image
            self.panel.place(x=620, y=40)
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    # Нанести водяной знак
    def send_image(self):
        try:
            if self.send_path != '':
                im = get_watermark_image(self.send_path)
                save_image(im)
                self.box.insert(END, '###   Водяной знак нанесён успешно   ###')
                self.display(ImageTk.PhotoImage(Image.open('Processed image.png').resize((650, 400))))
            else:
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))


win = MyWindow()
win.mainloop()



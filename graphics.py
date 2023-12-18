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

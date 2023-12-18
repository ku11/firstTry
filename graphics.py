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
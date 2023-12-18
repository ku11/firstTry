def display(self, image):
        try:
            self.clear_label_image()
            self.panel = Label(image=image)
            self.panel.image = image
            self.panel.place(x=620, y=40)
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))
import tkinter as tk
import os
from glob import glob
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        self.files = glob("../pics/*.jpg")
        self.index = 0
        self.img = ImageTk.PhotoImage(Image.open(self.files[self.index]))
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label_image = tk.Label(self)
        self.label_image['image'] = self.img
        self.label_image.pack()
        self.f = tk.Frame()
        self.f.pack()
        self.btnPrev = tk.Button(self.f, text='上一张', command=self.prev)
        self.btnPrev.pack(side=tk.LEFT)
        self.btnNext = tk.Button(self.f, text='下一张', command=self.next)
        self.btnNext.pack(side=tk.LEFT)

    def prev(self):
        self.showfile(-1)

    def next(self):
        self.showfile(1)

    def showfile(self, n):
        self.index += n
        if self.index < 0:
            self.index = len(self.files) - 1
        if self.index > (len(self.files) - 1):
            self.index = 0
        self.img = ImageTk.PhotoImage(Image.open(self.files[self.index]))
        self.label_image['image'] = self.img


root = tk.Tk()
root.title('图像浏览')
app = Application(master=root)
app.mainloop()
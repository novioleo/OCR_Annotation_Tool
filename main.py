import os
import tkinter as tk
from glob import glob
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        self.image_files = None
        self.size_of_images = 0
        self.index = 0
        self.master = master
        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(self, height=300, width=300)
        self.canvas.pack()
        self.img = None
        self.pack()
        self.init_bind()
        self.init_image_folder()

    def init_bind(self):
        # 绑定方向键
        self.master.bind('<Left>', lambda event: self.prev())
        self.master.bind('<Right>', lambda event: self.next())
        self.canvas.bind('<Button-1>', self.draw_point)

    def init_image_folder(self):
        # 只加载jpg和png的图片
        self.image_files = list(
            filter(lambda x: os.path.splitext(x)[1].lower() in {'.jpg', '.png'},
                   glob(os.path.join(filedialog.askdirectory(), '*'))))
        self.size_of_images = len(self.image_files)
        self.show_file(self.index)

    def prev(self):
        if self.image_files:
            self.show_file(-1)

    def next(self):
        if self.image_files:
            self.show_file(1)

    def draw_point(self, event, r=5):
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,fill='red',outline='red')

    def show_file(self, n):
        self.index += n
        if self.index < 0:
            self.index = self.size_of_images - 1
        if self.index > (self.size_of_images - 1):
            self.index = 0
        self.img = ImageTk.PhotoImage(Image.open(self.image_files[self.index]))
        width, height = self.img.width(), self.img.height()
        self.canvas.delete('all')
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0, 0, anchor=NW, image=self.img, tag='background')
        self.canvas.update()


root = tk.Tk()
root.title('图像浏览')
app = Application(master=root)
app.mainloop()

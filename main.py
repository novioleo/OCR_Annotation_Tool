import os
import tkinter as tk
from glob import glob
from tkinter import filedialog

from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        self.image_files = None
        self.size_of_images = 0
        self.index = 0
        self.master = master
        tk.Frame.__init__(self, master)
        self.pack()
        self.init_widget()
        self.init_bind()
        self.init_image_folder()

    def init_widget(self):
        # 初始化照片区域
        self.label_image = tk.Label(self)
        self.label_image.pack()

    def init_bind(self):
        # 绑定方向键
        self.master.bind('<Left>', lambda event: self.prev())
        self.master.bind('<Right>', lambda event: self.next())

    def init_image_folder(self):
        # 只加载jpg和png的图片
        self.image_files = list(
            filter(lambda x: os.path.splitext(x)[1].lower() in {'.jpg', '.png'},
                   glob(os.path.join(filedialog.askdirectory(), '*'))))
        self.size_of_images = len(self.image_files)
        self.showfile(self.index)

    def prev(self):
        if self.image_files:
            self.showfile(-1)

    def next(self):
        if self.image_files:
            self.showfile(1)

    def showfile(self, n):
        self.index += n
        if self.index < 0:
            self.index = self.size_of_images - 1
        if self.index > (self.size_of_images - 1):
            self.index = 0
        self.img = ImageTk.PhotoImage(Image.open(self.image_files[self.index]))
        self.label_image['image'] = self.img


root = tk.Tk()
root.title('图像浏览')
app = Application(master=root)
app.mainloop()

from tkinter import *
from PIL import ImageTk, Image


def click_button():
    # 在标签上添加背景图片
    label = Label(window, text="图片标签", justify=LEFT, image=label_picture, compound=CENTER, font=("华文行楷", 20), fg="white")
    label.pack()


window = Tk()
window.geometry('620x650')   # 窗口的大小 用小写英文字母 x 连接
window.geometry("+130+140")  # 窗口位置（距离屏幕左上角） 用 + 连接

# 创建一个标签类, [justify]:对齐方式
textLabel = Label(window, justify=CENTER, text="你会看到一个图片按钮, 点击后会有一个图片标签")  # 左对齐
textLabel.pack()

# 创建一个图片管理类
picture = ImageTk.PhotoImage(file='background.jpg')
label_picture = ImageTk.PhotoImage(file='label_picture.jpg')

# 在按钮上添加背景图片
button = Button(window, text='Button', relief=RAISED, image=picture, command=click_button)
button.pack()
window.mainloop()


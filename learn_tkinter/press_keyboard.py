from tkinter import *


def press_keyboard(event):
    print("点击的键盘字符为：", event.char)


window = Tk()
frame = Frame(window, width=200, height=200)
frame.bind("<Key>", press_keyboard)
frame.focus_set()
frame.pack()
window.mainloop()

from tkinter import *


def click_mouse(event):
    print("点击位置：", event.x, event.y)


window = Tk()
frame = Frame(window, width=200, height=200)
# <Button-1>鼠标左键 # <Button-2>鼠标中键
# <Button-3>鼠标右键 # <Button-4>滚轮上滚（Linux），<Button-5>滚轮下滚（Linux）
frame.bind("<Button-1>", click_mouse)
frame.pack()
window.mainloop()

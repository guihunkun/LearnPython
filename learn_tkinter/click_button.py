from tkinter import *
from tkinter import messagebox


def click_button(event):
    messagebox.showinfo(title='Click', message='哎呀，被你点了')
    # messagebox.showerror(title='错误消息框', message='您输入的信息不合法！')


window = Tk()
window.geometry('320x320')   # 窗口的大小 用小写英文字母 x 连接
window.geometry("+130+140")  # 窗口位置（距离屏幕左上角） 用 + 连接
# 属性 relief 为控件呈现出来的3D浮雕样式，有 FLAT(平的)、RAISED(凸起的)、SUNKEN(凹陷的)、GROOVE(沟槽状边缘)和 RIDGE(脊状边缘) 5种。
button = Button(window, relief=RAISED, width=20, text='来点我啊')
button.bind("<Button-1>", click_button)
button.pack()
window.mainloop()

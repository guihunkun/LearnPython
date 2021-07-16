from tkinter import *


window = Tk()
label = Label(window, text='第一个标签',\
                      bg='#d3fbfb',\
                      fg='blue',\
                      font=('华文新魏', 20),\
                      width=30,\
                      height=3,\
                      relief=SUNKEN)
label.pack()  # 简单的布局方法
# label.grid(column=10, row=10)  # 基于网格的布局
window.mainloop()

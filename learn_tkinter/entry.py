from tkinter import *

window = Tk()
window.geometry('320x200')
window.title('Label + Entry')
window.geometry('+400+300')
label = Label(window, text="密码")
label.pack(side=LEFT)
entry = Entry(window, fg='blue', font=('华文行楷', 20), bg='pink', width=10, bd=2, show='*')  # show='*' 将隐藏填写的内容
entry.pack(side=RIGHT)
window.mainloop()


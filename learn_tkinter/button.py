from tkinter import *


def click_button():
    print("输入的内容是 ： ", input.get())


window = Tk()
window.geometry('360x360')
window.title('Button')
lable = Label(window, relief=SUNKEN, text='请输入内容后点击按钮')
lable.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
input = Entry(window)
input.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)

button = Button(window, text='Button', relief=RAISED, command=click_button)
button.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

txt = Text(window)
txt.place()
window.mainloop()

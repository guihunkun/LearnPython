from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def close_window():
    messagebox.showwarning(title="警告", message="不许关闭，好好回答")
    return


def Love():
    love_win = Toplevel(window)
    love_win.geometry("360x300+540+360")
    love_win.title("LOVE")
    label = Label(love_win, text="好巧，我也喜欢你", font=("微软雅黑", 20))
    label.pack()
    label1 = Label(love_win, text="认识一下，加个微信呗", font=("微软雅黑", 20))
    label1.pack()
    input1 = Entry(love_win)
    input1.pack()
    button = Button(love_win, text="确定", width=10, height=1, command=close_all)
    button.pack()
    love_win.protocol("WM_DELETE_WINDOW", close_love)


def close_love():
    return


def close_all():
    window.destroy()


def close_no_love():
    messagebox.showinfo("再考虑一下", "再考虑一下呗")
    not_love()


# 点击不喜欢触发的事件
def not_love():
    no_love = Toplevel(window)
    no_love.geometry("300x90+540+360")
    no_love.title("LOVE")
    label = Label(no_love, text="再考虑考虑呗！", font=("微软雅黑", 25))
    label.pack()
    btn = Button(no_love, text="好的", width=10, height=1, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", close_no_love)


if __name__ == '__main__':
    window = Tk()
    # 窗口标题
    window.title("I Love You")
    # 窗口的大小, 用小写的 x 连接
    window.geometry("600x600")
    # 窗口位置（距离屏幕左上角） 用 + 连接
    window.geometry("+100+100")

    # 用户关闭窗口触发的事件
    window.protocol("WM_DELETE_WINDOW", close_window)

    label = Label(window, text="Hello,小仙女", font=("微软雅黑", 15), fg="black")
    label.pack()

    label_love = Label(window, text="喜欢我吗？", font=("微软雅黑", 15))
    label_love.pack()

    #  显示图片
    photo = ImageTk.PhotoImage(file='love.jpg')
    image_lable = Label(window, image=photo)
    image_lable.pack()

    love_button = Button(window, relief=RAISED, text="喜欢", width=15, height=1, command=Love)
    love_button.pack()

    not_love_button = Button(window, relief=RAISED, text="不喜欢", width=15, height=1, command=not_love)
    not_love_button.pack()

    window.mainloop()

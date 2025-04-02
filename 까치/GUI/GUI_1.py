import tkinter 
win = tkinter.Tk()
win.title('윈도우 생성하기')

lbl=tkinter.Label(win, text= '게임을시작하지')
lbl.pack()
lbl2=tkinter.Label(win, text=" hello world", bg= 'skyblue', fg='white', takefocus= 'true')
lbl2.pack(fill='x')
win.mainloop()
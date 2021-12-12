import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.geometry('300x300')
window.title('A or B')

def btn_click():
    text1 = txtA.get()
    text2 = txtB.get()
    if text1 == text2:
        messagebox.showinfo("Result", "True")
    else:
        messagebox.showinfo("Result", "False")

txtA = tkinter.Entry(width=20)
txtA.place(x=90, y=70)

txtB = tkinter.Entry(width=20)
txtB.place(x=90, y=120)

btn = tkinter.Button(text='Compare', command=btn_click)
btn.pack()
window.mainloop()
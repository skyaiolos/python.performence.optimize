from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='popup', message='Button pressed!')


window = Tk()
button = Button(window, text='press', command=reply)
# button_exit = Button(window, text='Exit', command=exit())
button.pack()
window.mainloop()

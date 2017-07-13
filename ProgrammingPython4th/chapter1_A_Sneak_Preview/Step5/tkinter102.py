from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


def main():
    window = MyGui()
    window.pack()
    window.mainloop()


if __name__ == '__main__':
    main()

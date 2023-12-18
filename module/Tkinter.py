from tkinter import Tk
from tkinter.messagebox import askokcancel, showinfo

from module.PrintLogs import writeInLogStartWork, writeInLogTheEnd
from module.DrawingClass import DrawingClass

from variables.size import width, height


class Tkinter:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')
        self.root.grid()

        self.title = title

        # Привязываем функцию on_closing к событию закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.bind('<Escape>', self.on_closing)


    def run(self):
        writeInLogStartWork()

        # init important class
        DrawingClass()

        self.root.mainloop()

    def on_closing(self):
        answer = askokcancel(f"Закрыть {self.title}", "Вы уверены, что хотите закрыть окно?")

        if answer:
            showinfo(  # window open after click "OK"
                title='Закрытие окно!',
                message='Окно закроется!'
            )
            self.root.quit()
            self.root.destroy()
            writeInLogTheEnd()


App = Tkinter('Game Coloring')

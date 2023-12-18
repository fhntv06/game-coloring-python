from tkinter import *
from variables.size import width, height
from module.CreateElements import CreateElements


class TestDrawingClass:
    def __init__(self):
        self.root = Tk()
        self.root.title('TestDrawingClass')
        self.root.geometry(f'{width}x{height}')
        self.root.grid()

        self.closeButton = CreateElements('button', {'command': self.closeWindow, 'grid': {'column': 0, 'row': 0}})

    def closeWindow(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()


test = TestDrawingClass()

test.run()

from tkinter import Button, Canvas
from module.PrintLogs import writeInLog, writeLogAndExit


class CreateElements:
    def __init__(self, name, params):
        dictionary_elements = {
            'button': self.create_button,
            'canvas': self.create_canvas,
        }

        self.name = name
        self.params = params

        func_create_by_name = dictionary_elements.get(self.name)

        if not func_create_by_name:
            writeLogAndExit(f'Нет элемента с тегом: {self.name}')
        else:
            self.element = func_create_by_name()

    def create_canvas(self):
        canvas = Canvas(width=250, height=250, background='gray')
        return canvas

    def create_button(self):
        command = self.params.get('command') or writeInLog(f'Функция не задана на {self.name} при создании элемента')
        grid = self.params.get('grid') or {'column': 1, 'row': 1}  # default
        text = self.params.get('text') or f'Text не задан для {self.name}'

        button = Button(text=text, background='gray', command=command)
        button.grid(column=grid['column'], row=grid['row'])

        return button

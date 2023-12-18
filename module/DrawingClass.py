import sys
from module.PrintLogs import writeInLog
from module.CreateElements import CreateElements


class DrawingClass:
    def __init__(self):
        CreateElements(
            'button',
            {
                'command': lambda: writeInLog('Click by example button'),
                'grid': {'column': 2, 'row': 2},
                'text': 'Print in log'
            }
        )

# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime


class Datetime:
    def __init__(self):
        # Получаем текущее время
        self.current_datetime = datetime.now()

        self.values = {
            'day': self.current_datetime.day,
            'month': self.current_datetime.month,
            'year': self.current_datetime.year,
            'hour': self.current_datetime.hour,
            'minute': self.current_datetime.minute,
            'second': self.current_datetime.second,
            'all': [
                self.current_datetime.day,
                self.current_datetime.month,
                self.current_datetime.year,
                self.current_datetime.hour,
                self.current_datetime.minute,
                self.current_datetime.second,
            ]
        }

    def getHourInMinutes(self, hour='hour'):
        forming_minutes = hour if isinstance(hour, (int, float)) else self.values.get('hour')
        return forming_minutes * 60

    def getCtime(self):
        return time.ctime()

    def getAllDateAndTime(self, state=False):
        day, month, year, hour, minute, second = self.getDatetimeCorrect('all')

        return f'{day}{month}{year}_{hour}{minute}{second}' \
            if state \
            else f'{day}/{month}/{year} {hour}:{minute}:{second}'

    def dispenseValue(self, value):
        return f'0{value}' if value < 10 else value

    def formingCorrectStringDate(self, value):
        return list(map(self.dispenseValue, value)) if type(value) == list else self.dispenseValue(value)

    def getDatetimeCorrect(self, selector):
        value = self.values.get(selector)

        return self.formingCorrectStringDate(value)

    def getDatetime(self, selector):
        return self.values.get(selector)


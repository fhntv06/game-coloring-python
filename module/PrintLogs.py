import sys
from module.Datetime import Datetime
from variables.common import file_log


class PrintLogs:
    def __init__(self):
        self.date_time = Datetime()

    def writeInLog(self, message, is_error=False):
        correct_message = f"\033[1;30m\u274C\033[0m\033[1;31m {message}\033[40m" \
            if is_error \
            else f"\033[3;32m\u21E8\033[0m {message}"

        symbol = '❌' if is_error else '⇨'

        with open(file_log, "a") as file:
            print(correct_message + '\n')
            file.write(symbol + ' ' + message + '\n')

    def writeLogAndExit(self, message):
        text_end_script = f"Остановил выполнение скрипта в {self.date_time.getAllDateAndTime()}"
        self.writeInLog(message, True)
        self.writeInLog(text_end_script, True)
        sys.exit()

    def writeInLogStartWork(self):
        self.writeInLog(f'============================== BOOT ==============================')
        self.writeInLog(f"Скрипт запущен в {self.date_time.getAllDateAndTime()}!\n")

    def writeInLogTheEnd(self):
        self.writeInLog(f'\nЗавершил работу в {self.date_time.getAllDateAndTime()}')
        self.writeInLog('============================== The End ==============================\n')


print_logs = PrintLogs()

writeInLog = print_logs.writeInLog
writeLogAndExit = print_logs.writeLogAndExit
writeInLogStartWork = print_logs.writeInLogStartWork
writeInLogTheEnd = print_logs.writeInLogTheEnd

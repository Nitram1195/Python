#!/usr/bin/env python3
"""
Logger
"""

import sys


class Logger():
    """
    Logger
    """
    
    def __init__(self, name):
        self._name = name
        self._level = 0
        self._printers = []
    
    
    def set_level(self, level):
        self._level = level
        
    
    def log(self, level, message):
        if level > self._level:
            for p in self._printers:
                p.print(message)
    
    def add_printer(self, printer):
        self._printers.append(printer)
        

class Printer_std():
    """
    Standart output printer
    """


    def print(self, message):
        sys.stdout.write(message)

class Printer_err():
    """
    Error output printer
    """
    

    def __init__(self, formater):
        self._formater = formater

    def print(self, message):
        sys.stderr.write(formater.format(message))


class Formater_datetime():
    """
    Formated date time output
    """    
    import datetime
    

    def format (self, logger, message):
        return str(datetime.data.now()) + logger._name + ": " + message


if __name__ == "__main__":
    loger = Logger("Logger1")
    f1 = Formater_datetime()
    printerStandart = Printer_std()
    printerError = Printer_err(f1)
    loger.add_printer(printerStandart)
    loger.add_printer(printerError)
    loger.log(2,f1.format(logger,"Ahoj"))


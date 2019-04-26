#!/usr/bin/env python3
"""
Logger
"""

import sys
import datetime
from abc import ABC, abstractmethod


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
                p.print(self, message)

    def add_printer(self, printer):
        self._printers.append(printer)


class Printer_std():
    """
    Standart output printer
    """

    def __init__(self, formater=None):
        self._formater = formater


    def print(self, logger, message):
        if self._formater:
            sys.stdout.write(self._formater.format(logger, message))
        else:
            sys.stdout.write(message)


class Printer_err():
    """
    Error output printer
    """


    def __init__(self, formater=None):
        self._formater = formater

    def print(self, logger, message):
        if self._formater:
            sys.stderr.write(self._formater.format(logger, message))
        else:
            sys.stderr.write(message)


class Formater(ABC):
    """
    Formated abstrace base class
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def format(self):
        pass

class Formater_datetime(Formater):
    """
    Formated date time output
    """
    def __init__(self):
        super().__init__()


    def format(self, logger, message):
        return str(datetime.datetime.now()) +logger._name +": " + message + "\n"


class Formated_name(Formater):
    """
    Formated name output
    """
    def __init__(self):
        super().__init__()

    def format(self, logger, message):
        return logger._name +": " + message + "\n"


if __name__ == "__main__":
    loger = Logger("Logger1")
    f1 = Formater_datetime()
    printerStandart = Printer_std()
    printerError = Printer_err(f1)
    loger.add_printer(printerStandart)
    loger.add_printer(printerError)
    loger.log(2, "ahoj")

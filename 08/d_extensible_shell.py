#!/usr/bin/env python3
"""
Extensible shell
"""
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract class for command
    """
    def __init__(self):
        super().__init__()


    @abstractmethod
    def help(self):
        pass


    @abstractmethod
    def get_name(self):
        pass


    @abstractmethod
    def execute(self):
        pass


class CommandHelp(Command):
    """
    Command help
    """
    def __init__(self):
        super().__init__()
        self._name = "Help"


    def help(self):
        print("returns all posiible commands")


    def get_name(self):
        return self._name


    def execute(self, shell):
        for comm in shell._commands:
            print(comm.get_name())


class Shell():
    """
    Shell
    """
    def __init__(self):
        help_com = CommandHelp()
        self._commands = [help_com]


    def launch(self):
        """
        Launch the shell
        """
        while True:
            text = input()
            for command in self._commands:
                if command.get_name() == text:
                    command.execute(self)


if __name__ == "__main__":
    SHELL1 = Shell()
    SHELL1.launch()

#!/usr/bin/env python3
from abc import ABC, abstractmethod
import sys


class Processor():
    def __init__(self, plugins):
        self._plugins = plugins
        self._text = ""

    def zpracuj(self):
        self.input_text()
        self.process()
        print(self._text)

    def input_text(self):
        self._text = input()
    
    def process(self):
         for plugin in self._plugins:
             self._text = plugin.process(self._text)


class Plugin(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def process(self, text):
        pass


class PluginUpper(Plugin):
    def __init__(self):
        super().__init__()
        self._name = "Uppercase"

    def name(self):
        return self._name

    def process(self, text):
        return text.upper()

class PluginLower(Plugin):
    def __init__(self):
        super().__init__()
        self._name = "Lowercase"

    def name(self):
        return self._name

    def process(self, text):
        return text.lower()


class PluginRW(Plugin):
    def __init__(self):
        super().__init__()
        self._name = "Remove white spaces"

    def name(self):
        return self._name

    def process(self, text):
        return text.replace(" ","")


if __name__ == "__main__":
    plugins = []
    for i in sys.argv:
         if i == "upper":
             pu = PluginUpper() 
             plugins.append(pu)
         elif i == "lower":
             pl = PluginLower()
             plugins.append(pl)
         elif i == "rmw":
             prw = PluginRW()
             plugins.append(prw)
    proc = Processor(plugins)
    proc.zpracuj()

#!/usr/bin/env python3
"""
Displa file
"""

import sys


def display_files():
    soubory = sys.argv
    for i in range(1,len(soubory)):
        with open (soubory[i]) as f:
            for line in f:
                print(line,end="")
                volba = input()
                if volba == "n":
                    break
                elif volba == "q":
                    sys.exit(0)

if __name__ == "__main__":
    display_files()
    

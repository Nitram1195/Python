#!/usr/bin/env python3
"""
Postfix calculator
"""


def spust_kalkulacku():
    """
    spusti kalkulacku
    """
    while True:
        try:
            text = input()
            znaky = text.split()
            if znaky:
                vypocti(znaky)
        except EOFError:
            break


def vypocti(znaky):
    """
    vypocita ulohu
    """
    stack = []
    try:
        for znak in znaky:
            if znak == "+":
                stack[-2] = stack[-2]+stack[-1]
                del stack[-1]
            elif znak == "-":
                stack[-2] = stack[-2]-stack[-1]
                del stack[-1]
            elif znak == "*":
                stack[-2] = stack[-2]*stack[-1]
                del stack[-1]
            elif znak == "/":
                stack[-2] = stack[-2]//stack[-1]
                del stack[-1]
            else:
                stack.append(int(float(znak)))
        if len(stack) == 1:
            print(stack[0])
        else:
            print("Malformed expression")
    except ZeroDivisionError:
        print("Zero division")
    except:
        print("Malformed expression")


if __name__ == "__main__":
    spust_kalkulacku()

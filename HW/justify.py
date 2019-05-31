#!/usr/bin/env python3


import sys


def zarovnej_do_bloku(delka):
    text = ""
    prvni = True
    for line in sys.stdin:
        if len(line.strip()) == 0 and len(text) != 0:
            zpracuj_odstavec(text, delka, prvni)
            prvni = False
            text =""
        elif len(line.strip()) == 0 and len(text) == 0:
            continue
        else:
            text += line
    if len(text) != 0:
        zpracuj_odstavec(text, delka, prvni)
        prvni = False


def zpracuj_odstavec(text, delka, prvni):
    slova = text.split()
    delka_textu = 0
    radky = []
    slova_na_radku =  []
    for slovo in slova:
        if len(slovo) + delka_textu > delka:
            radky.append(slova_na_radku)
            slova_na_radku = [slovo]
            delka_textu = len(slovo) + 1
        else:
            slova_na_radku.append(slovo)
            delka_textu += (len(slovo) + 1)
    if slova_na_radku:
        radky.append(slova_na_radku)
    vysledny_text = []
    for r in radky[0:-1]:
        vysledny_text.append(pridej_mezery(r, delka))
    pos_radka = " ".join(radky[-1])
    vysledny_text.append(pos_radka)
    if prvni == False:
        print("")
    for v in vysledny_text:
        print(v)


def pridej_mezery(text, delka):
    if len(text) > 1:
        m_vsude = (delka - len("".join(text))) // (len(text)-1)
        m_nekde = (delka - len("".join(text))) % (len(text)-1)
        v_text_1 = ((1+m_vsude)*" ").join(text[0:m_nekde+1])
        v_text = (m_vsude*" ").join([v_text_1]+text[m_nekde+1:])
    else:
        v_text = "".join(text)
    return v_text
   

if __name__ == "__main__":
    try:
        delka = int(sys.argv[1])
    except ValueError:
        print("Error",end="")
    except IndexError:
        print("Error",end="")
    else:
        if delka < 1:
            print("Error",end="")
        else:
            zarovnej_do_bloku(delka)

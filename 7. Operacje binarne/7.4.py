import math
obwód_drzewa = int(input(f'podaj obwód drzewa: '))
średnica_drzewa = obwód_drzewa / math.pi
ścięcie = średnica_drzewa >= 50
print(f'Drzewo można sciąć: {ścięcie}')
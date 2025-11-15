import random

wyrzucona_liczba = random.randint(1,6)
jest_specjalna = (wyrzucona_liczba == 1) or (wyrzucona_liczba == 6)

print(f'Wyrzucona liczba to: {wyrzucona_liczba}')
print(f'Wyrzucona liczba jest specjalna: {jest_specjalna}')
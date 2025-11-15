import math
promień = int(input(f'Podaj promień koła: '))
pole_koła = math.pi * (promień ** 2)
obwód_koła = 2 * math.pi * promień
print(f'Pole koła wynosi: {pole_koła:.2f} jednostki 2.')
print(f'Obwód koła wynosi: {obwód_koła:.2f} jednostki.')
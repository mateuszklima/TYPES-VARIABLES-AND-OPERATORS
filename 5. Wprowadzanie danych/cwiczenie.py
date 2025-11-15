kwota_za_danie = float(input(f"Podaj kwotę jedzenia: "))
napiwek = kwota_za_danie * 0.15
calkowita_kwota = kwota_za_danie + napiwek
print(f"Koszta jedzenia: {kwota_za_danie:.2f} zł.")
print(f"Napiwek wynosi: {napiwek:.2f} zł.")
print(f"Całkowita kwota do zapłaty: {calkowita_kwota:.2f} zł.")
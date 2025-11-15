cena_produktu = float(input(f"Podaj cene produktu: "))
rabat_produktu = float(input(f"Podaj ile procent wynosi rabat: "))
rabat = cena_produktu * (rabat_produktu / 100)
cena_produktu_po_obniżce = cena_produktu - rabat
różnica = cena_produktu - cena_produktu_po_obniżce
print(f"Cena początkowa wynosi: {cena_produktu:.2f} zł")
print(f"Rabat produktu wynosi: {rabat_produktu:.2f} %")
print(f"Cena po obniżce wynosi: {cena_produktu_po_obniżce:.2f} zł")
print(f"Różnica pomiędzy ceną początkową a ceną po rabacie wynosi: {różnica:.2f} zł")
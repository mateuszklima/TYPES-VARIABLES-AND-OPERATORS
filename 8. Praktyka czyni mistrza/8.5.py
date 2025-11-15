###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Podaj kod SWIFT: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[0:2]}')
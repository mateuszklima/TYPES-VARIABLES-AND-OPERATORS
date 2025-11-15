
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ').upper() #upper robi to że program oblicza również duże litery
last = input('Enter last letter: ').upper()
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(last_letter_code - first_letter_code) - 1 #abs zwraca zawsze wartość dodatnią, nieważne czy wynik był dodatni czy ujemny
print(f'Between {first} and {last} is {number_of_letters} letters')
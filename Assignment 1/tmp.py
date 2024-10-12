import math
def letter_to_number(letter):
    # Converti una lettera in un numero (a = 1, b = 2, ..., z = 26)
    return ord(letter.lower()) - ord('a') + 1
def number_to_letter(number):
    # Modifica per gestire numeri che superano 26, mantenendoli nel range alfabetico
    number = (number - 1) % 26 + 1
    return chr(number + ord('a') - 1)


stringa = "abc"
a1 = [letter_to_number(char) for char in stringa]
n1 = 0
for e in a1:
    n1 += e
stringa2 = "bcd"
a2 = [letter_to_number(char) for char in stringa2]
n2 = 0
for e in a2:
    n2 += e


media = (n1 + n2)/2
up = math.ceil(media)
down = math.floor(media)
print(f"{n1=} {n2=} {media=}")
print(f"{down=} {up=}")

str1 = number_to_letter(n1)
str2 = number_to_letter(n2)
print(f"{str1=} {str2=}")
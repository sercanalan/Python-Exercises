"""
Koşul 1-> Şifrede hem büyük harf hem de küçük harf kullanılması gerek.

Koşul 2-> Şifre içerisinde bir sayı kullanılmış olması gerek.

Koşul 3-> Şifrenin 8 karakterden uzun olması gerek.

Koşul 4-> Şifrenin 16 karakterden kısa olması gerek.

"""

number_of_characters = 0
lowercase_letter = False
uppercase_letter = False
isNumber = False

password = input("Şifre: ")

for x in password:
    number_of_characters += 1

    if (lowercase_letter == False and x >= "a" and x <= "z"):
        lowercase_letter = True
    
    if (uppercase_letter == False and x >= "A" and x <= "Z"):
        uppercase_letter = True

    if (isNumber == False and x >= "0" and x <= "9"):
        isNumber = True

if (lowercase_letter == False and uppercase_letter == False):
    print("Harf kullanılmadı!")
elif (isNumber == False):
    print("Sayı kullanılmadı!")
elif (lowercase_letter == False):
    print("Küçük harf kullanılmadı!")
elif (uppercase_letter == False):
    print("Büyük harf kullanılmadı!")
elif (number_of_characters < 8 or number_of_characters > 16):
    print("Şifre en az 8, en fazla 16 karakter olmalıdır.")
else:
    print("Şifre oluşturuldu.")
"""
0!=1

1!=1

2!=2x1=2

3!=3x2x1=3

4!=4x3x2x1=24
"""

number = int(input("Faktöriyeli Hesaplanacak Sayı: "))
factorial = 1

if number < 0:
    print("Lütfen Negatif Sayı Girmeyiniz...")
elif number > 0:
    iterator=1
    while iterator<=number:
        factorial *= iterator
        iterator +=1
    print("{}! = {}".format(number,factorial))
else:
    print("{}! = {}".format(number,factorial))



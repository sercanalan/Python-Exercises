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
    for i in range(1,number+1):
        factorial *= i
    print("{}! = {}".format(number,factorial))
else:
    factorial = 1
    print("{}! = {}".format(number,factorial))
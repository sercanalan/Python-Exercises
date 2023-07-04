"""
number1 = 4
number2 = 6

EBOB = 2  --> 4 % ebob == 0 and 6 % ebob == 0 (number1 < number 2 --> maks EBOB = number1. So, iteration should count up to SmallerNumber)

EKOK = 12 --> ekok % 4 == 0 and ekok % 6 == 0 (min EKOK: bigger_number) 
"""

number1= int(input("İlk Sayı: "))
number2= int(input("İkinci Sayı: "))

smaller_number = number1
if (number2 < number1):
    smaller_number = number2

bigger_number = number1
if (number2 > number1):
    bigger_number = number2

# EBOB
ebob = 1

i=1
while (i <= smaller_number):
    if (number1 % i == 0) and (number2 % i == 0):
        ebob = i
    i += 1

# EKOK
ekok = bigger_number
while (True):
    if (ekok % number1 == 0 and ekok % number2 == 0):
        break
    ekok += 1



print("\nEBOB: {}\nEKOK: {}".format(ebob,ekok))
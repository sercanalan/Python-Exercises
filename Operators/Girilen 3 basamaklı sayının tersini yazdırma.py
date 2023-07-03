"""
---SAMPLE OUTPUT---
Girilen sayı: 123

İlk iterasyonda sayı:123, yazdırılan basamak: 3

İkinci iterasyonda sayı:12, yazdırılan basamak: 2

Üçüncü iterasyonda sayı: 1, yazdırılan basamak: 1

"""

number = int(input("Girilen Sayı: "))

print("İlk iterasyonda sayı:{}, yazdırılan basamak: {}".format(number,number%10))
reversed_number = number%10
number = number // 10


print("İkinci iterasyonda sayı:{}, yazdırılan basamak: {}".format(number,number%10))
reversed_number = (reversed_number*10)+(number%10)
number = number // 10


print("Üçüncü iterasyonda sayı: {}, yazdırılan basamak: {}".format(number,number%10))
reversed_number = (reversed_number*10)+(number%10)

print("Ters sayı: {}".format(reversed_number))
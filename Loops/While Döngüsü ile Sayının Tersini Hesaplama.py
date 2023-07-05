"""
number = 123 , temp

number % 10 = 3 (reverse_number = 3 = 0*10 + 3)
temp = number // 10 = 12

number % 10 = 2 (reverse_number = 32 = 3*10 + 2)
temp = number // 10 = 1

number % 10 = 1 (reverse_number = 321 = 32*10 + 1)
temp = number // 10 = 0 --> break
"""

number = int(input("Sayı: "))
temp = number

reverse_number = 0
while(temp != 0):
    reverse_number = (reverse_number*10) + (temp % 10)
    temp = temp // 10

print("Ters Sayı: ",reverse_number)
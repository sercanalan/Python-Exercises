"""
number = 12345      (digit = 0)

12345 // 10 = 1234  (digit = 1)
1234 // 10 = 123    (digit = 2)
123 // 10 = 12      (digit = 3)
12 // 10 = 1        (digit = 4)
1 // 10 = 0         (digit = 5)
0 --> break
"""

number = int(input("Girilen Sayı "))
temp = number

digit = 0

while not (temp == 0):
    temp = temp // 10
    digit += 1

print("{} Sayısı, {} Basamaklıdır.".format(number,digit))
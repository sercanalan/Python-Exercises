"""
number = 5
--> 5 % 1 = 0
5 % 2 != 0
5 % 3 != 0
5 % 4 != 0
--> 5 % 5 = 0
"""

number = int(input("Girilen Sayı "))

for iterator in range(2,number):
    if (number % iterator == 0):
        print("{} Sayısı Asal Değildir.".format(number))
        break
    elif (number % iterator != 0) and (iterator == number-1):
        print("{} Sayısı Asaldır.".format(number))
        break


"""
----Other Way to Solve----
number = int(input("Sorgulanacak sayiyi giriniz:"))
isDivided = False

for i in range(2,number):
    if (number % i == 0):
        isDivided = True
        break
        
if isDivided:
    print("{} Sayısı Asal Değildir.".format(number))
else:
    print("{} Sayısı Asaldır.".format(number))
"""
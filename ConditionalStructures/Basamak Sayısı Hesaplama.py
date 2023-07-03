# Maksimum 5 basamaklı üreteceğiniz bir rastgele sayının kaç basamaklı olduğunu hesaplayın.

import random

random_number = random.randint(1,99999)
temp = random_number

number_of_digit = 0

while(temp != 0):
        temp = temp // 10
        number_of_digit +=1
    
print("Girilen {} sayısı {} basamaklıdır.".format(random_number,number_of_digit))
"""
Fonksiyon dışarıdan 2 sayı alacak ve Recursive olarak EBOB-EKOK değerlerini hesaplayacak. 
Bunun için GCD algoritmasını inceleyebilirsiniz

"""

def recursiveEBOB(number1,number2):
    if (number2 == 0):
        return number1
    return recursiveEBOB(number2, number1 % number2)

def recursiveEKOK(number1,number2):
    return number1*number2//recursiveEBOB(number1,number2)
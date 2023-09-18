"""
Fonksiyon dışarıdan bir string alacak ve stringteki ünlü harflerin sayısını yazdıracak

unluHarfler=['a','e','i','u','o']

"""

def counterOfVowels(str):
    listOfStr = list(str)

    numberOfVowels = 0

    for x in range(len(listOfStr)):

        if (listOfStr[x]=='a' or listOfStr[x]=='A' or
            listOfStr[x]=='e' or listOfStr[x]=='E' or
            listOfStr[x]=='i' or listOfStr[x]=='I' or
            listOfStr[x]=='u' or listOfStr[x]=='U' or
            listOfStr[x]=='o' or listOfStr[x]=='O'):
            
            numberOfVowels += 1

    print("Sesli Harf Sayısı:",numberOfVowels)
    

enteredString = input("Bir Cümle Giriniz: ")
counterOfVowels(enteredString)
"""
Fonksiyon dışarıdan bir cümle alacak ve cümledeki kelime ve karakter sayısını hesaplayacak.

"""
def numberOfCharacters_Letters(sentence):
    sentence = sentence.strip()             # Cümlenin başını ve sonunu boşluklardan arındırdı
    listOfSentence = list(sentence)         # Cümle listeye çevrildi
    
    numberOfCharacter = 0
    numberOfLetter = 1

    for x in range(len(listOfSentence)):    # Liste uzunluğunda döngü oluşturuldu
        if (listOfSentence[x] != " "):      
            numberOfCharacter += 1

        if (listOfSentence[x-1] == " " and ((listOfSentence[x] >= 'A' and listOfSentence[x] <= 'Z') or (listOfSentence[x] >= 'a' and listOfSentence[x] <= 'z') )):
            numberOfLetter += 1

    if (numberOfCharacter == 0):             # Karakter girilmediyse kelime de oluşmaz
        numberOfLetter = 0

    print ("""
            Karakter Sayısı: {}
            Kelime Sayısı: {}
            """.format(numberOfCharacter,numberOfLetter))



sentence = input("Girilen Cümle: ")
numberOfCharacters_Letters(sentence)



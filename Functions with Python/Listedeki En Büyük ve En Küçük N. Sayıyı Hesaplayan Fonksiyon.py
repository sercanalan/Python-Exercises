"""
Fonksiyon dışarıdan bir liste ve bir N sayısı alacak, sırasıyla listenin en büyük ve en küçük N. sayısını return edecek

Örneğin liste: 1,54,32,65,23,93, N sayısı 2 ise

65 ve 23 sonuçlarını döndürecek

"""


def largestN_SmallestN(enteredList,N):
    enteredList.sort()

    largestN = enteredList[-N]
    smallestN = enteredList[N-1]
    
    return largestN,smallestN 


largestN,smallestN = largestN_SmallestN([1,54,32,65,23,93],2)

print("""
        En Büyük N. Sayı: {}
        En Küçük N. Sayı: {}

     """.format(largestN,smallestN))
"""
---SAMPLE OUTPUT---
Girilen tutar: 1480

İlk girilen tutar: 1480TL=7 adet 200 TL bulunmaktadır.

Geriye kalan tutar: 80TL=0 adet 100 TL bulunmaktadır.

Geriye kalan tutar: 80TL=1 adet 50 TL bulunmaktadır.

Geriye kalan tutar: 30TL=1 adet 20 TL bulunmaktadır.

Geriye kalan tutar: 10TL=1 adet 10 TL bulunmaktadır.

Geriye kalan tutar: 0TL= 0 adet 5 TL bulunmaktadır.

"""

money = int(input("Enter a number: "))

a1 = money // 200
k1 = money % 200

a2 = k1 // 100 
k2 = k1 % 100

a3 = k2 // 50 
k3 = k2 % 50

a4 = k3 // 20 
k4 = k3 % 20

a5 = k4 // 10
k5 = k4 % 10

a6 = k5 // 5 
k6 = k5 % 5

print("""
    Girilen tutar: {}

    İlk girilen tutar: {}TL={} adet 200 TL bulunmaktadır.

    Geriye kalan tutar: {}TL={} adet 100 TL bulunmaktadır.

    Geriye kalan tutar: {}TL={} adet 50 TL bulunmaktadır.

    Geriye kalan tutar: {}TL={} adet 20 TL bulunmaktadır.

    Geriye kalan tutar: {}TL={} adet 10 TL bulunmaktadır.

    Geriye kalan tutar: {}TL= {} adet 5 TL bulunmaktadır.
   
    """.format(money,money,a1,k1,a2,k2,a3,k3,a4,k4,a5,k5,a6) 
    )
"""
Kullanıcıdan bir üçgenin üç kenar bilgisini alın, ardından bu 3 kenar bilgisine göre (x,y,z) 
bir üçgen oluşturulabiliyor mu bunu kontrol edin.

Koşul 1-> x kenarı için: |y-z| < x < y+z olmalı 
Koşul 2-> y kenarı için: |x-z| < y < x+z olmalı 
Koşul 3-> z kenarı için: |x-y| < z < x+y olmalı
"""

x,y,z=map(int,input("Lutfen sirasiyla 3 kenar bilgisini ',' ile ayirarak giriniz: ").split(","))
        # map(int,input("")) fonksiyonu input olarak alınan stringi int'e çevirir.
        # input("").split(,) fonksiyonu alınan değerlerin virgülle ayrılarak girilmesini ister (Örn: 1,2,3) 

if abs(y-z)>=x or x>=y+z:
    print("x kenari ucgen sartini saglamiyor!")
elif abs(x-z)>=y or y>=x+z:
    print("y kenari ucgen sartini saglamiyor!")
elif abs(x-y)>=z or z>=x+y:
    print("z kenari ucgen sartini saglamiyor!")
else:
    print("Ucgen olusabilir!")
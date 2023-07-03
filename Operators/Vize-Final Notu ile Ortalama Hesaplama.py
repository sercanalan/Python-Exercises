"""
Kullanıcıdan; vize ve final notlarını isteyerek aşağıdaki sınav yüzdelerine göre ders ortalamasını hesaplayın. 
Ardından eğer ki ders ortalaması 60'dan büyükse konsola True, değilse False yazdırın.

Ortalama Hesaplama Yüzdesi: Final-> %60, Vize-> %40
"""

midterm = float(input("Vize Notu: "))

final = float(input("Final Notu: "))

mean = (midterm*0.4)+(final*0.6) 
print("Ortalama: {}".format(float(mean)))

print("""
    Ortalama > 60 : {}
    Ortalama < 60 : {}
    Ortalama = 60 : {}
    """.format(mean > 60, mean < 60, mean == 60))
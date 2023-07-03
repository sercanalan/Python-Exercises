"""
Kullanıcıdan; yarıçap değerini isteyerek aşağıdaki formüllere göre daire'nin çevresini ve alanını hesaplayın.

Daire Alan Formulü:pi*r^2

Daire Çevre Formulü:2pir
"""
from math import *

radius = int(input("Daire Yarıçapı(r): "))

print("Dairenin Alanı: {}\nDairenin Çevresi: {}".format(pi*(radius**2),2*pi*radius))
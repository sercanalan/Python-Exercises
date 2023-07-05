"""
cumle="a bcd e f"

1.İterasyon: Harf-> "a", boslukSayisi=0

2.İterasyon: Harf-> " ", boslukSayisi=1

3.İterasyon: Harf-> "b", boslukSayisi=1

4.İterasyon: Harf-> "c", boslukSayisi=1

5.İterasyon: Harf-> "d", boslukSayisi=1

6.İterasyon: Harf-> " ", boslukSayisi=2

7.İterasyon: Harf-> "e", boslukSayisi=2

8.İterasyon: Harf-> " ", boslukSayisi=3

9.İterasyon: Harf-> "f", boslukSayisi=3
"""

sentence = input("Cümle: ")

space = 0

for c in sentence:
    if c == " ":
        space += 1

print("Boşluk Sayısı: ",space)
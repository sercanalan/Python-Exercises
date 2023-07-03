"""
Bir fiyat hesaplama programı yaptığınızı düşünün, 
kullanıcının taksit isteyip istemediği ve alışveriş kartının olup olmadığına göre fiyat güncellemesi yapın.

Koşul 1-> Eğer ki taksit istiyorsa 3 taksit için %3, 6 taksit için %6, 9 taksit için %9 fiyat artışı olacak. 
Koşul 2-> Eğer ki alışveriş kartı varsa, %10 indirim sağlanacak
"""

price = float(input("Ürünün Etiket Fiyatı: "))

installment_choice = input("""
    ---Lütfen Taksit Seçeneklerinden Birini Seçiniz---
        1) 3 Taksit   (%3 Vade Farkı Uygulanır)
        2) 6 Taksit   (%6 Vade Farkı Uygulanır)
        3) 9 Taksit   (%9 Vade Farkı Uygulanır)
        4) Taksit İstemiyorum

        Seçimim: """)


shopping_card_choice = input("""
    ---Alışveriş Kartınız Var mıdır?---
        1) Evet   (%10 İndirim Fırsatı)
        2) Hayır
        
        Seçimim: """)


if(installment_choice == "1" and shopping_card_choice == "1"):
    print("3 Taksit ve Alışveriş Kartı ile Ödeme Tutarı: ",(price*1.03)*0.9)
elif(installment_choice == "2" and shopping_card_choice == "1"):
    print("6 Taksit ve Alışveriş Kartı ile Ödeme Tutarı: ",(price*1.06)*0.9)
elif(installment_choice == "3" and shopping_card_choice == "1"):
    print("9 Taksit ve Alışveriş Kartı ile Ödeme Tutarı: ",(price*1.09)*0.9)
elif(installment_choice == "4" and shopping_card_choice == "1"):
    print("Taksitsiz ve Alışveriş Kartı ile Ödeme Tutarı: ",price*0.9)
elif(installment_choice == "1" and shopping_card_choice == "2"):
    print("3 Taksit ve Alışveriş Kartsız Ödeme Tutarı: ",price*1.03)
elif(installment_choice == "2" and shopping_card_choice == "2"):
    print("6 Taksit ve Alışveriş Kartsız Ödeme Tutarı: ",price*1.06)
elif(installment_choice == "3" and shopping_card_choice == "2"):
    print("9 Taksit ve Alışveriş Kartsız Ödeme Tutarı: ",price*1.09)    
elif(installment_choice == "4" and shopping_card_choice == "2"):
    print("Taksitsiz ve Alışveriş Kartsız Ödeme Tutarı: ",price)
else:
    print("Yeniden Deneyin")
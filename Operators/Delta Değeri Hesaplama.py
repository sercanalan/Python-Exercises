"""
Kullanıcıdan; a,b,c değerlerini isteyerek aşağıdaki formule göre delta değerini hesaplayın. 
Ardından delta değerinin sıfırdan büyük mü yoksa küçük mü olduğuna göre konsola True-False yazdırın

Delta Hesaplama Formulü:b^2-4ac
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = (b**2)-(4*a*c)


print("""
    Delta = {}
    Delta > 0: {}
    Delta < 0: {}
    Delta = 0: {}

    """.format(delta,delta>0,delta<0,delta==0)
    )
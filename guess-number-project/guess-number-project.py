from random import random
import random
sayi = random.randint(1,100)
can = int(input("Kaç Hak İstersiniz: "))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))
    if sayi == tahmin:
        print(f"Tebrikler {sayac}.de bildiniz Bildiniz.Toplam Puanınınz: {100-(100/can)*(sayac-1)} ")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşşağı")
    if hak == 0:
        print(f"hakkınız bitti.Tutulan sayı: {sayi} ")





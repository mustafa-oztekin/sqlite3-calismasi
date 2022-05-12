import time

from main import *

print("""
***************************************
Kütüphane programına hoşgeldiniz....

İşlemler;

1.Kitapları Göster

2.Kitap Sorgula

3.Kitap Ekle

4.Kitap Sil

5.Baskı Yükselt

Çıkmak için 'q' ya basın.
***************************************""")

kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız işlem:")

    if (işlem == "q"):
        print("program sonlandırılıyor....")
        break
    elif (işlem == "1"):
        kütüphane.kitaplari_goster()

    elif (işlem == "2"):
        isim = input("hangi kitabı istiyorsunuz:")
        print("kitap sorgulanıyor")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("yazar:")
        yayın = input("yayınevi:")
        tür = input("tür:")
        baskı = int(input("baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayın,tür,baskı)

        print("kitap ekleniyor")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi")


    elif (işlem == "4"):
        isim = input("hangi kitabı silmek istiyorsunuz:")
        cevap = input("emin misiniz ? (E/H)")

        if (cevap == "E"):
            print("kitap siliniyor")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("kitap silindi")

    elif (işlem == "5"):
        isim = input("hangi kitabın baskısını yükseltmek istiyorsunuz:")
        print("baskı yükseltiliyor")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("baskıyükseltildi....")


    else:
        print("geçersiz işlem...")























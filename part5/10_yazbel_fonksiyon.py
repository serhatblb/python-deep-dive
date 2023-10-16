import random

print("Serhat", "Bülbül", "1995", "Istanbul")


def kayit_olustur(ad, soyad, yas, sehir):
    print("-" * 50)

    print("Ad:", ad)
    print("Soyad:", soyad)
    print("Yas:", yas)
    print("Sehir:", sehir)

    print("-" * 50)


kayit_olustur("Serhat", "Bülbül", "27", "Istanbul")
kayit_olustur("Ahmet", "Bülbül", "27", "Istanbul")


def sistem_bilgisi_göster():
    import sys

    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)


sistem_bilgisi_göster()

# bir sayinin karesini yazan fonksiyonu yazınız.


def kare_bul(sayı):
    çıktı = "{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı, sayı**2))


def kare_bul(sayı):
    çıktı = "{} sayısının karesi {}, karekökü ise {} sayısıdır"
    print(çıktı.format(sayı, sayı**2, sayı**0.5))


kare_bul(5)
kare_bul(54354)
kare_bul(4)

a = 0
for b in 'serhat':
    a += 1
print(a)

# alternatif len() fonksiyonu
def uzunluk(öğe):
    c = 0
    for s in öğe:
        c += 1
    print(c)


uzunluk('serhat')

print('\n')
print("######-parametre-######")
print('\n')


def kopyala(kaynak_dosya, hedef_dizin):
    çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
    print(çıktı.format(kaynak_dosya, hedef_dizin))


kopyala("deneme.txt", "/home/istihza/Desktop")

print('\n')


def kur(kurulum_dizini="/usr/bin/"):
    print("Program {} dizinine kuruldu!".format(kurulum_dizini))


kur()
kur("/home/istihza/Desktop/")

print('\n')


def fonksiyon(**parametreler):
    print(parametreler)


fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")


def karşılık_bul(*args, **kwargs):
    for sözcük in args:
        if sözcük in kwargs:
            print("{} = {}".format(sözcük, kwargs[sözcük]))
        else:
            print("{} kelimesi sözlükte yok!".format(sözcük))


sözlük = {"kitap": "book", "bilgisayar": "computer", "programlama": "programming"}

karşılık_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)


def bas(*args, start='', **kwargs):
    for öğe in args:
        print(start + öğe, **kwargs)


bas('öğe1', 'öğe2', 'öğe3', start="#.")


# def ismin_ne():
#     isim = input("ismin ne? ")
#     return isim


# print(ismin_ne())


def fonk(n):
    if n < 0:
        return 'eksi değerli sayı olmaz!'
    else:
        return n


f = fonk(-5)
print(f)


def sayi_uret(baslangic=0, bitis=500, adet=6):
    sayilar = set()

    while len(sayilar) < adet:
        sayilar.add(random.randint(baslangic, bitis))

    return sayilar


print(sayi_uret())
# print(dir(random))
liste = ["ahmet", "mehmet", "sevgi", "sevim", "selin", "zeynep", "selim"]
print(random.choice(liste))
print(random.shuffle(liste))
print(liste)
for i in range(100):
    print(sayi_uret(1, 10, 2))

print('\n')

isim = 'Fırat'


def fonk():
    isim += ' Özgül'
    return isim


print(fonk())

import random

deste = ["A", "2", "3", "4", "5", "6", "7",
"8", "9", "T", "J", "Q", "K"]
# 10'ları tek haneli olması için T olarak saklayacağız

deste2 = deste*4*6
random.shuffle(deste2)
#deste artık karıştı

para = 10000
mevcutbahis = 0
sonbahis = "Henüz yapılmadı"
minbahis = 100
maxbahis = 5000

kasanin_eli = None
kasanin_eldegeri = None
# ornek kasa eli A J
# kasa elinin değeri 21

oyuncu_eli = None
oyuncu_eldegeri = None



# J Q K leri 10a çevirme
def onlari_cevir(dizi_formatinda_el):
    dizi_formatinda_el2 = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "J" or dizi_formatinda_el2[i] == "Q" or dizi_formatinda_el2[i] == "K" or dizi_formatinda_el2[i] == "T":
            # T 10'u temsil eden tek haneli bir karakterdir
            dizi_formatinda_el2[i] = "10"
    return dizi_formatinda_el2


# A'ları 1'e çevirme
def aslari_cevir(dizi_formatinda_el):
    dizi_formatinda_el2 = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "A":
            dizi_formatinda_el2[i] = "1"
    return dizi_formatinda_el2


def kartlarin_degerlerini_topla(dizi_formatinda_el):
    toplam = 0
    for i in range(len(dizi_formatinda_el)):
        toplam += int(dizi_formatinda_el[i])
    # toplama bitti sonucu döndürüyoruz
    return toplam


def el_degeri_bul(el):
    #el bir list
    deger1 = 0
    deger2 = 0
    dizi_el = list(el)
    dizi_el_yedek = list(el)


    # J Q K leri 10a çevirme
    dizi_el = list(onlari_cevir(dizi_el))


    # El değeri bulma:

    # Durum 1: Eğer elde A yoksa:
    if "A" not in dizi_el:
        # eldeki kartların değerini tek tek toplama
        deger1 = kartlarin_degerlerini_topla(dizi_el)

    # Durum 2: Eğer elde A varsa 
    else:
        """bu kisim ileride silinecek (başlangic)"""
        A_11_kabul_edildi = False
        # A bir kez 11 kabul edildikten sonra geri kalan tüm A'lar 1 kabul edilecek.
        
        # (Çünkü 2 tane A'nın 11 kabul edilmesi AA gibi bir elde 22 elde etmemize sebep olur onun yerine
        # ilk A'yı 11 kabul edip 2.sini 1 kabul edebiliriz ve 12 buluruz
        # veya her iki A'yı da 1 kabul ederiz ve 2 buluruz)
        """bu kisim ileride silinecek (bitis)"""

        dizi_el = list(aslari_cevir(dizi_el))
        
        # buradaki işlemleri anlamak için dosyanın sonundaki açıklamayı oku
        deger1 = kartlarin_degerlerini_topla(dizi_el)
        deger2 = deger1 + 10


    sonuc = [deger1, deger2]
    return sonuc










"""
Eğer kartlar 4 ve A ise
değer 5 ve 15tir
A = 1 ise sonuç: 4 + 1'den 5'tir
A = 11 ise sonuç: 4 + 11'den 15tir
yani sonuç x ve x + 10'dur
Fakat deger2'ye her zaman x+10 demek yanlış olabilir çünkü eğer el zaten 16 falansa as çekildiğinde sonuç 16 + 11den 27 olur bunun yerine elin patlamaması için A'yı 1 kabul etmek zorundayız
Değer1de A'yı her zaman 1 kabul edeceğiz
Değer2de ilk A'yı 11 sonraki A'ları 1 kabul edeceğiz (Çünkü AA yani 2 tane A her ikisinide 11 kabul edersek 22 olup patlıyor.
O yüzden -patlamayı engellemek için- mecburen ilk A'dan sonraki tüm A'ları 1 kabul etmek zorundayız.)
"""
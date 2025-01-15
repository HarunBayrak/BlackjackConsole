import random

# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# J Q K leri 10a çevirme
def onlari_cevir(dizi_formatinda_el):
    dizi_formatinda_el2 = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "J" or dizi_formatinda_el2[i] == "Q" or dizi_formatinda_el2[i] == "K" or dizi_formatinda_el2[i] == "T":
            # T 10'u temsil eden tek haneli bir karakterdir
            dizi_formatinda_el2[i] = "10"
    return dizi_formatinda_el2

# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# A'ları 1'e çevirme
def aslari_cevir(dizi_formatinda_el):
    dizi_formatinda_el2 = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "A":
            dizi_formatinda_el2[i] = "1"
    return dizi_formatinda_el2

# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# Bu fonksiyon sayı tabanlı kartların değerini toplar yani el değerini hesaplar 
# Fakat A cinsi kartları sayamaz bu yüzden "el_degeri_hesapla()" fonksiyonu içerisinde kullanılması gereklidir. 
# Böylece A'lar 1'e ve 11'e çevrilir ve artık destede harf kalmadığı için el değeri rahatça hesaplanabilir.
def kartlarin_degerlerini_topla(dizi_formatinda_el):
    toplam = 0
    for i in range(len(dizi_formatinda_el)):
        toplam += int(dizi_formatinda_el[i])
    # toplama bitti sonucu döndürüyoruz
    return toplam


def el_degeri_hesapla(el):
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



def listi_stringe_donustur(verilen_list):
    string_listesi = []
    
    # Verilen listenin üzerinde geziniyoruz
    for i in verilen_list:
        # Elemanları tek tek stringe dönüştürüyoruz
        string_oge = str(i)
        string_listesi.append(string_oge)
    
    # Öğeleri ", " ile ayırıyoruz
    sonuc = ", ".join(string_listesi)
    
    return sonuc


def fn_karar(parametre_el: list, parametre_bakiye: int, parametre_bahis: int) -> None:

    # eğer split_mumkun_mu fonksiyonu False döndürüyorsa, karar metninden split seçeneği kaldırılabilir, ve ona rağmen split seçilirse split mümkün değil denebilir
    def split_mumkun_mu(parametre2_el: list, parametre2_bakiye: int, parametre2_bahis: int) -> bool:
        if parametre2_el[0] == parametre2_el[1] and parametre2_bahis < parametre2_bakiye:
            return True
        else:
            return False


    def double_icin_bakiye_yeterli_mi(parametre3_bakiye: int, parametre3_bahis: int) -> bool:
        if parametre3_bahis < parametre3_bakiye:
            return True
        else:
            return False


    while True:
        karar = input(
            "Ne yapmak istiyorsunuz:\n" +
            "1. Hit\n" +
            "2. Double\n" +
            "3. Split\n" +
            "4. Stand\n"
        ).lower()

        if (karar != "1" or
            karar != "2" or
            karar != "3" or
            karar != "hit" or
            karar != "double" or
            karar != "split" or
            karar != "stand"):

            if karar == "1" or karar == "hit":
                return 1
            
            elif karar == "2" or karar == "double":
                if double_icin_bakiye_yeterli_mi(parametre_bakiye, parametre_bahis):
                    return 2
                else:
                    print("\nDouble atmak için yeterli bakiyeniz yok!\n")
                    continue

            
            elif karar == "3" or karar == "split":
                if split_mumkun_mu(parametre_el, parametre_bakiye, parametre_bahis):
                    return 3
                else:
                    print("\nKartlarınız aynı değil veya split işlemi için yeterli bakiyeniz yok!\n")
                    continue

            elif karar == "4" or karar == "stand":
                return 4

            else:
                print("\nİşlem seçimini hatalı girdiniz! Tekrar denemeniz gerekiyor.\n")



def ic_oyun_dongusu():

    deste = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # 10'ları tek haneli olması için T olarak saklayacağız

    deste2 = deste*4*6
    random.shuffle(deste2)
    #deste artık karıştı

    para = 10000
    mevcutbahis = 0
    sonbahis = "Henüz yapılmadı"
    minbahis = 100
    maxbahis = 5000

    kasanin_eli = list()
    kasanin_eldegeri = 0
    # ornek kasa eli A J
    # kasa elinin değeri 21

    oyuncunun_eli = list()
    oyuncu_eldegeri = 0
    #2024-08-25

    mevcutbahis = int(input(f"{para} Paran var, bahis kaç tl olsun: "))
    para -= mevcutbahis
    print(f"""\
          Para: {para}
          Bahis: {mevcutbahis}""")

    # kart çekme işlemi çekilen kartı desteden silip, kartı kart çeken kişiye verir
    kasanin_eli += [deste2.pop(0)]
    kasanin_eli += [deste2.pop(0)]
    kasanin_eldegeri = el_degeri_hesapla(kasanin_eli)
    #print("kasa el değeri", kasanin_eldegeri)

    oyuncunun_eli += [deste2.pop(0)]
    oyuncunun_eli += [deste2.pop(0)]
    oyuncu_eldegeri = el_degeri_hesapla(oyuncunun_eli)

    if oyuncu_eldegeri[1] == 0:
        oyuncu_gercek_deger = oyuncu_eldegeri[0]
    else:
        if int(oyuncu_eldegeri[1]) < 22:
            oyuncu_gercek_deger = int(oyuncu_eldegeri[1])
        else:
            oyuncu_gercek_deger = int(oyuncu_eldegeri[0])

    #print("oyuncunun el değeri", oyuncu_eldegeri)

    str_kasanin_eli = listi_stringe_donustur(kasanin_eli)
    str_oyuncunun_eli = listi_stringe_donustur(oyuncunun_eli)
    print(f"""Kasanın eli: {str_kasanin_eli}\
          Oyuncunun eli: {str_oyuncunun_eli}\n""")

    str_karar = fn_karar(oyuncunun_eli, para, mevcutbahis)
    if str_karar == 1: # Hit
        # Hit seçildiği için "oyuncu_eli"ne kart eklenmeli
        # oyuncu 21in üstüne çıkarsa (patlarsa) direkt kaybeder ve kasanın elini görür.
        oyuncunun_eli += [deste2.pop(0)]
        oyuncu_eldegeri = el_degeri_hesapla(oyuncunun_eli)

    elif str_karar == 2: # Double
        # Double seçildiği için "oyuncu_eli"ne 1 kart eklenmeli ve sanki stand seçmiş gibi davranılmalı.
        # Sonuç gösterme kısmını hem stand'de hem de double'da tekrar kodlamaya gerek yok. O yüzden direkt stand'deki kısım çalıştırılabilir.
        pass
    elif str_karar == 3: # Split
        # Karar fonksiyonundan Split mümkün olduğunu belirten değer gelirse, deste 2'ye bölünecek ve her 2 ele de birer kart dağıtılacak, 
        # çünkü blackjack'te oyuncu her zaman 2 kartla başlar. Yani el 2'ye bölünüp, bölünmüş kısımlara 1'er kart verilecek.
        # Detaylı açıklamayı aşağıda bulabilirsin. 
        pass
    elif str_karar == 4: # Stand
        # Stand sonrası kart çekme durmalı ve sonuç ekranı gelmeli. Eğer kasanın eli 17den küçükse kasa 17ye kadar kart çeker.
        # Daha sonra kimse patlamadıysa eli daha büyük olan kazanır. Eğer kasanın ve oyuncunun eli eşit ise beraberedir ve oyuncu parasını geri alır.
        # Eğer oyuncu patladıysa oyuncu kaybeder. Zaten hit kısmında oyuncu kart çekip patlarsa yapılacakların kodu olacak.
        # Eğer kasa patlar ise ve oyuncu patlamadıysa oyuncu kazanır.
        pass
    

"""
Split mümkün mü karar fonksiyonu kontrol ediyor zaten. Eğer karar fonksiyonu splitin mümkün olmadığını belirten bir değer gönderirse, split mümkün değil çıktısı gösterilmeli. Eğer Split mümkünse oyuncu için ikinci bir el oluşturulmalı. Örneğin [8, 8] olan el, [8] , [8] şeklinde ikiye bölünmeli. Daha sonra her biri için kart çekip çekmek istemediğinin soran karar fonksiyonu çağırılmalı. Splitten sonra split de mümkün örneğin 8,8 olan asıl deste 1. el: 8, 3 ve 2. el 8, 8 olarak bölünmüş olabilir bu durumda oyununcunun tekrar split çalıştırmasına izin verilmeli bu da tüm bu karar kısmını tekrar split içine koymamız gerektiğini gösteriyor örneğin:


str_karar = fn_karar(oyuncunun_eli, para, mevcutbahis)
if str_karar == 1: # Hit
    # Hit seçildiği için "oyuncu_eli"ne kart eklenmeli
    # oyuncu 21in üstüne çıkarsa (patlarsa) direkt kaybeder ve kasanın elini görür.
    pass
elif str_karar == 2: # Double
    # Double seçildiği için "oyuncu_eli"ne 1 kart eklenmeli ve sanki stand seçmiş gibi davranılmalı.
    # Sonuç gösterme kısmını hem stand'de hem de double'da tekrar kodlamaya gerek yok. O yüzden direkt stand'deki kısım çalıştırılabilir.
    pass
elif str_karar == 3: # Split
    ################ Aynı döngünün içteki versiyonu
    str_karar = fn_karar(oyuncunun_eli, para, mevcutbahis)
    if str_karar == 1: # Hit
        # Hit seçildiği için "oyuncu_eli"ne kart eklenmeli
        # oyuncu 21in üstüne çıkarsa (patlarsa) direkt kaybeder ve kasanın elini görür.
        pass
    elif str_karar == 2: # Double
        # Double seçildiği için "oyuncu_eli"ne 1 kart eklenmeli ve sanki stand seçmiş gibi davranılmalı.
        # Sonuç gösterme kısmını hem stand'de hem de double'da tekrar kodlamaya gerek yok. O yüzden direkt stand'deki kısım çalıştırılabilir.
        pass
    elif str_karar == 3: # Split
        pass
    elif str_karar == 4: # Stand
        # Stand sonrası kart çekme durmalı ve sonuç ekranı gelmeli. Eğer kasanın eli 17den küçükse kasa 17ye kadar kart çeker.
        # Daha sonra kimse patlamadıysa eli daha büyük olan kazanır. Eğer kasanın ve oyuncunun eli eşit ise beraberedir ve oyuncu parasını geri alır.
        # Eğer oyuncu patladıysa oyuncu kaybeder. Zaten hit kısmında oyuncu kart çekip patlarsa yapılacakların kodu olacak.
        # Eğer kasa patlar ise ve oyuncu patlamadıysa oyuncu kazanır.
        pass
    ############## iç döngünün bitişi
elif str_karar == 4: # Stand
    # Stand sonrası kart çekme durmalı ve sonuç ekranı gelmeli. Eğer kasanın eli 17den küçükse kasa 17ye kadar kart çeker.
    # Daha sonra kimse patlamadıysa eli daha büyük olan kazanır. Eğer kasanın ve oyuncunun eli eşit ise beraberedir ve oyuncu parasını geri alır.
    # Eğer oyuncu patladıysa oyuncu kaybeder. Zaten hit kısmında oyuncu kart çekip patlarsa yapılacakların kodu olacak.
    # Eğer kasa patlar ise ve oyuncu patlamadıysa oyuncu kazanır.
    pass

"""



def dis_oyun_dongusu():
    while True:
        ic_oyun_dongusu()




dis_oyun_dongusu()





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
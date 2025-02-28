import random
from typing import List

# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# J Q K leri 10a çevirme
def onlari_cevir(dizi_formatinda_el: List[str]) -> List[str]:
    dizi_formatinda_el2: List[str] = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "J" or dizi_formatinda_el2[i] == "Q" or dizi_formatinda_el2[i] == "K" or dizi_formatinda_el2[i] == "T":
            # T 10'u temsil eden tek haneli bir karakterdir
            dizi_formatinda_el2[i] = "10"
    return dizi_formatinda_el2


# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# A'ları 1'e çevirme
def aslari_cevir(dizi_formatinda_el: List[str]) -> List[str]:
    dizi_formatinda_el2: List[str] = list(dizi_formatinda_el)
    for i in range(len(dizi_formatinda_el2)):
        if dizi_formatinda_el2[i] == "A":
            dizi_formatinda_el2[i] = "1"
    return dizi_formatinda_el2


# Bu fonksiyon verilen elin değerini hesaplayan "el_degeri_hesapla()" fonksiyonunun ihtiyaç duyduğu bir araçtır.
# Bu fonksiyon sayı tabanlı kartların değerini toplar yani el değerini hesaplar 
# Fakat A cinsi kartları sayamaz bu yüzden "el_degeri_hesapla()" fonksiyonu içerisinde kullanılması gereklidir. 
# Böylece A'lar 1'e ve 11'e çevrilir ve artık destede harf kalmadığı için el değeri rahatça hesaplanabilir.
def kartlarin_degerlerini_topla(dizi_formatinda_el: List[str]) -> int:
    toplam: int = 0
    for i in range(len(dizi_formatinda_el)):
        toplam += int(dizi_formatinda_el[i])
    # toplama bitti sonucu döndürüyoruz
    return toplam


def el_degeri_hesapla(el: List[str]) -> List[int]:
    #el bir list
    deger1: int = 0
    deger2: int = 0
    dizi_el: List[str] = list(el)
    dizi_el_yedek: List[str] = list(el)


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
        A_11_kabul_edildi: bool = False
        # A bir kez 11 kabul edildikten sonra geri kalan tüm A'lar 1 kabul edilecek.
        
        # (Çünkü 2 tane A'nın 11 kabul edilmesi AA gibi bir elde 22 elde etmemize sebep olur onun yerine
        # ilk A'yı 11 kabul edip 2.sini 1 kabul edebiliriz ve 12 buluruz
        # veya her iki A'yı da 1 kabul ederiz ve 2 buluruz)
        """bu kisim ileride silinecek (bitis)"""

        dizi_el = list(aslari_cevir(dizi_el))
        
        # buradaki işlemleri anlamak için dosyanın sonundaki açıklamayı oku
        deger1 = kartlarin_degerlerini_topla(dizi_el)
        deger2 = deger1 + 10


    sonuc: List[int] = [deger1, deger2]
    return sonuc


def listi_stringe_donustur(verilen_list: List[str]) -> str:
    string_listesi: List[str] = []
    
    # Verilen listenin üzerinde geziniyoruz
    for i in verilen_list:
        # Elemanları tek tek stringe dönüştürüyoruz
        string_oge: str = str(i)
        string_listesi.append(string_oge)
    
    # Öğeleri ", " ile ayırıyoruz
    sonuc: str = ", ".join(string_listesi)
    
    return sonuc


def fn_karar(parametre_el: list, parametre_bakiye: int, parametre_bahis: int) -> int:

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
            "\nNe yapmak istiyorsunuz:\n" +
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


def gercek_degeri_ver(eller: List[int]) -> int:
    final_deger: int = None
    if eller[1] != 0 and eller[1] < 22:
        final_deger = eller[1]
    else:
        final_deger = eller[0]
    # Elde A varsa patlamayan en büyük el değerini aldık.
    return final_deger

def ic_oyun_dongusu() -> None:

    deste: List[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # 10'ları tek haneli olması için T olarak saklayacağız

    deste2: List[str] = list(deste*4*6)
    random.shuffle(deste2)
    #deste artık karıştı

    para: int = 10000
    mevcutbahis: int = 0
    sonbahis: int = 0
    minbahis: int = 100
    maxbahis: int = 5000

    while True:
        kasanin_eli: List[str] = list()
        kasanin_eldegeri: int = 0
        # ornek kasa eli A J
        # kasa elinin değeri 21

        oyuncunun_eli: List[str] = list()
        oyuncu_eldegeri: int = 0
        #2024-08-25
        mevcutbahis = int(input(f"\n{para} Paranız var, bahis kaç tl olsun: "))
        sonbahis = mevcutbahis
        para -= mevcutbahis # bahis kadar paraya el koyuyoruz
        print(f"""\
            Para: {para}
            Bahis: {mevcutbahis}""")

        # kart çekme işlemi çekilen kartı desteden silip, kartı kart çeken kişiye verir
        kasanin_eli += [deste2.pop(0)]
        kasanin_eli += [deste2.pop(0)]
        kasanin_el_degerleri: List[int] = el_degeri_hesapla(kasanin_eli)
        #print("kasa el değeri", kasanin_eldegeri)

        oyuncunun_eli += [deste2.pop(0)]
        oyuncunun_eli += [deste2.pop(0)]
        oyuncunun_eldegerleri: List[int]= el_degeri_hesapla(oyuncunun_eli)
        #elde_as_var: bool = False
        #as_11iken_patlama: bool = False
        
        # Yukarıdaki şu aslı bool değişkenleri hiç kullanmayabilirim.
        if oyuncunun_eldegerleri[1] == 0:
            oyuncu_gercek_deger: int = oyuncunun_eldegerleri[0]
        else:
            if int(oyuncunun_eldegerleri[1]) < 22:
                oyuncu_gercek_deger = int(oyuncunun_eldegerleri[1])
            else:
                oyuncu_gercek_deger = int(oyuncunun_eldegerleri[0])

        #print("oyuncunun el değeri", oyuncu_eldegeri)
        kasanin_eli_yedek: List[str] = list(kasanin_eli)
        kasanin_eli_yedek[1] = "X"
        str_kasanin_eli_sansursuz = listi_stringe_donustur(kasanin_eli)
        str_kasanin_eli_sansurlu = listi_stringe_donustur(kasanin_eli_yedek)
        str_oyuncunun_eli = listi_stringe_donustur(oyuncunun_eli)

        oyuncunun_el_degeri_final: int = gercek_degeri_ver(oyuncunun_eldegerleri)

        print(f"""Kasanın eli: {str_kasanin_eli_sansurlu}\
            Oyuncunun eli: {str_oyuncunun_eli} ({oyuncunun_el_degeri_final})""")
        while True:
            str_karar = fn_karar(oyuncunun_eli, para, mevcutbahis)
            print("")
            if str_karar == 1: # Hit
                # Hit seçildiği için "oyuncu_eli"ne kart eklenmeli
                # oyuncu 21in üstüne çıkarsa (patlarsa) direkt kaybeder ve kasanın elini görür.
                oyuncunun_eli += [deste2.pop(0)]
                oyuncunun_eldegerleri: List[int]= el_degeri_hesapla(oyuncunun_eli)
                str_oyuncunun_eli = listi_stringe_donustur(oyuncunun_eli)
                oyuncunun_el_degeri_final: int = gercek_degeri_ver(oyuncunun_eldegerleri)
                kasanin_el_degeri_final: int = gercek_degeri_ver(kasanin_el_degerleri)
                print("Kart çektiniz, eliniz artık:", str_oyuncunun_eli, f"({oyuncunun_el_degeri_final})")
                if oyuncunun_eldegerleri[0] > 21:
                    print("Patladınız! ", end="")
                    print(f"Kasanın eli: {str_kasanin_eli_sansursuz} ({kasanin_el_degeri_final}) idi.")
                    # bahis parasına en başta el koyulduğu için burada el kaybedildiğinde parayı eksiltmeye gerek yok
                    break
                else:
                    continue

            elif str_karar == 2: # Double
                # Double seçildiği için "oyuncu_eli"ne 1 kart eklenmeli ve sanki stand seçmiş gibi davranılmalı.
                # Sonuç gösterme kısmını hem stand'de hem de double'da tekrar kodlamaya gerek yok. O yüzden direkt stand'deki kısım çalıştırılabilir.
                print("\nDouble daha kodlanmadı!\n")
                continue

            elif str_karar == 3: # Split
                # Karar fonksiyonundan Split mümkün olduğunu belirten değer gelirse, deste 2'ye bölünecek ve her 2 ele de birer kart dağıtılacak, 
                # çünkü blackjack'te oyuncu her zaman 2 kartla başlar. Yani el 2'ye bölünüp, bölünmüş kısımlara 1'er kart verilecek.
                # Detaylı açıklamayı aşağıda bulabilirsin.
                print("\nSplit daha kodlanmadı!\n")
                continue

            elif str_karar == 4: # Stand
                # Stand sonrası kart çekme durmalı ve sonuç ekranı gelmeli. Eğer kasanın eli 17den küçükse kasa 17ye kadar kart çeker.
                # Daha sonra kimse patlamadıysa eli daha büyük olan kazanır. Eğer kasanın ve oyuncunun eli eşit ise beraberedir ve oyuncu parasını geri alır.
                # Eğer oyuncu patladıysa oyuncu kaybeder. Zaten hit kısmında oyuncu kart çekip patlarsa yapılacakların kodu olacak.
                # Eğer kasa patlar ise ve oyuncu patlamadıysa oyuncu kazanır.

                oyuncunun_el_degeri_final: int = gercek_degeri_ver(oyuncunun_eldegerleri)
                kasanin_el_degeri_final: int = gercek_degeri_ver(kasanin_el_degerleri)

                #önce kasanın 2 kartlı mevcut elini oyuncuya gösteriyoruz:
                print(f"Oyuncunun eli: {str_oyuncunun_eli} ({oyuncunun_el_degeri_final}) \n")
                print(f"Kasanın eli: {str_kasanin_eli_sansursuz} ({kasanin_el_degeri_final}) \n")
                # Kasanın çekip çekmeyeceğinin kontrolü:

                # Eğer kasanın eli, A kartı 11 olarak kabul edilse de, edilmese de 16dan büyükse kasanın final eli bu değerdir.

                if kasanin_el_degeri_final < 17: # yani kasanın eli 17den küçükse, kasa 16dan büyük bir el elde edene veya patlayana kadar kart çekmek zorundadır.
                    print("Kasanın eli 17den küçük, kasa kart çekmek zorunda...", "\n")
                    while kasanin_el_degerleri[0] < 17 and kasanin_el_degerleri[1] < 17:
                        kasanin_eli += [deste2.pop(0)]
                        kasanin_el_degerleri = el_degeri_hesapla(kasanin_eli)
                        str_kasanin_eli_sansursuz = listi_stringe_donustur(kasanin_eli)
                        kasanin_el_degeri_final = gercek_degeri_ver(kasanin_el_degerleri)
                        print(f"Kasa kart çekti artık yeni eli: {str_kasanin_eli_sansursuz} ({kasanin_el_degeri_final}) \n")
                    #artık döngünün dışına çıkıldığına göre kasa ya patladı ya da 17 veya üzerine üzerine çıktı
                    kasanin_el_degeri_final = gercek_degeri_ver(kasanin_el_degerleri)

                # Kimin kazandığının kontrolü:
                # burayı elif yapma, burası sonuç ne olursa olsun çalışmalı
                if kasanin_el_degeri_final > 21:
                    print("Kasa patladı, oyuncu kazandı")
                    #para artış kodu
                    para += (2 * mevcutbahis)
                    break

                else: # eğer kasa patlamadıysa kasa ve oyununun arasından daha büyük ele sahip olan kazanır.
                    if oyuncunun_el_degeri_final > kasanin_el_degeri_final:
                        print("mevcut bahis:", mevcutbahis)
                        para += (2 * mevcutbahis)
                        print("Oyuncu kazandı!\n", "Yeni bakiye: ", para, "\n\n")
                        break
                    elif oyuncunun_el_degeri_final < kasanin_el_degeri_final:
                        # bahis parasına en başta el koyulduğu için burada el kaybedildiğinde parayı eksiltmeye gerek yok
                        print("Kasa kazandı.\n", "Mevcut bakiye: ", para, "\n\n")
                        break
                    else:
                        para += mevcutbahis
                        print("Berabere!")
                        break











    
# muhtemelen AA durumu 2 kabul edilecek ileride bu olası bug'ı düzelt




def dis_oyun_dongusu() -> None:
    while True:
        ic_oyun_dongusu()




#dis_oyun_dongusu()
ic_oyun_dongusu()

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
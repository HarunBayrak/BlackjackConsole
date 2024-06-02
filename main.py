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

oyuncu_eli = None
oyuncu_eldegeri = None
#ornek kasa eli A J
#      kasa elinin değeri 21



def el_degeri_bul(el):
    #el bir list
    deger1 = 0
    deger2 = None
    dizi_el = list(el)


    # J Q K leri 10a çevirme
    for i in range(len(dizi_el)):
        if dizi_el[i] == "J" or el[i] == "Q" or el[i] == "K" or el[i] == "T":
            # T 10'u temsil eden tek haneli bir karakterdir
            dizi_el[i] = "10"

    if "A" not in dizi_el:
        # 10a çevirdikten sonra dümdüz toplama
        deger1 = int(dizi_el[0]) + int(dizi_el[1])

    else:
        #A varsa yapılacaklar
        for i in range(len(dizi_el)):
            if dizi_el[i] == "A":
                dizi_el[i] = "1"

    for i in range(len(dizi_el)):
        deger1 += int(dizi_el[i])

    if "A" in el and deger1 <= 21:
        deger2 = deger1 + 10

    sonuc = [deger1, deger2]
    return deger1

#sadace çağırdığımız noktada gelir
#kod tekrarını önler.
#definition tanımlama demek
def OrtalamaHesapla() :
    final = 100
    vize = 85
    ortalama= (vize*0.4) + (final*0.6)
    print(ortalama)

def OrtalamaHesapla2():
    final = 100
    vize = 85
    ortalama= (vize*0.4) + (final*0.6)
    return ortalama
#return ifadesi fonksiyonun çağırıldığı yere değer götürür. return ekrana yazdırmıyor sadece değeri döndürüyor.

OrtalamaHesapla()
OrtalamaHesapla2() #print etmediğimiz için yazmıyor.
print(OrtalamaHesapla2()) 

def OrtalamaHesaplat(vize : float, final: float) -> float: #okunabilirliği arttırmak için. 
    #vize float, final float, sonuç da float dönebilir. sonucu yazmaya gerek olmayabilir anlıyor zaten.
    return (vize*0.4) + (final*0.6) #değer döndürdüğü için return şeklinde yazabilirim
    
print(OrtalamaHesaplat(86, 45))




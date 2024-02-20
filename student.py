# ---Bir okul kayıt sistemi kodlayalım---
# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. 
# Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek 
# bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. 
# Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

class Student:
    def __init__(self, isim, soyisim):
        self.isim= isim
        self.soyisim= soyisim
        
    
    def bilgi(self):
        print(f"öğrenci adı: {self.isim}, soyadı: {self.soyisim}")
    
    def ortalamaHesaplama(self, vize, final):
        ortalama= (vize*0.4) + (final*0.6)
        print(f"Ortalamanız: {ortalama}")

student1= Student("ayşe", "yılmaz")
student2= Student("ali", "kaya")
student1.bilgi()
student1.ortalamaHesaplama(70, 80)
student2.bilgi()
student2.ortalamaHesaplama(50, 100)

    

    
        


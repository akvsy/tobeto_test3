from student import Student
from teacher import Teacher

student1= Student("ayşe", "yılmaz")
student2= Student("ali", "kaya")
teacher1= Teacher("Nesibe", "Kaya", "Matematik")
teacher2= Teacher("Ahmet", "Tanış", "Fizik")
teacher3= Teacher("Özlem", "Akman", "Edebiyat")
teacher4= Teacher("Kevser", "Yılmaz", "Kimya")

ogrenciListesi= []
ogretmenListesi= []

def ogrenciEkle(ogrenci):
    ogrenciListesi.append(ogrenci)

ogrenciEkle(student1)
print(ogrenciListesi)
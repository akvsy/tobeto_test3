from student import Student
from teacher import Teacher

ogrenciListesi=[]
ogretmenListesi=[]

def addStudent(isim,soyisim,vize,final):
    newStudent=Student(isim,soyisim,vize,final)
    ogrenciListesi.append(newStudent)


def printStudent():
    for student in ogrenciListesi:
        student.bilgi()
        adSoyad= student.isim+ " " +student.soyisim
        print(f"{adSoyad} ortalamanız:  {student.ortalamaHesaplama()}")

def addTeacher(isim,soyisim,bolum,maas,zamOrani):
    newTeacher=Teacher(isim,soyisim,bolum,maas,zamOrani)
    ogretmenListesi.append(newTeacher)

def printTeacher():
    for teacher in ogretmenListesi:
        teacher.bilgi()
        print(f"Zamlı maaşınız=", teacher.zamliMaas())


    

addStudent("Nesibe","Kaya",70,80)
addStudent("Kevser","Yılmaz",100,80)
addTeacher("Özlem","Akman","Matematik",10000,30)
addTeacher("Emir","Yılmaz","Fizik",12000,20)

printStudent()
printTeacher()

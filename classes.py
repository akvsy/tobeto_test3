#nesne tabanlı dolayısıyla her şey bir sınıftır.
#fonksiyonlar yerine method değişkenler yerine attribute kullanıcaz.
#nesne, obje, sınıf da denir classa.

name= "irem"
age= "25"


def Age(age):
    return age

#sınıf oluşturmak istiyorum. özellikler olan bir sınıf.
#artık değşkenlerim sınıfın attribute u olmuş oldu.
#fonksiyonları aldığımda methodu olmuş olud.
#class oluşturmak aslında kalıp oluşturmak.


class Human():
    #property, attribute => özellik, nitelik
    name = ""
    age = "25"

    #davranışlar, method
    def Age(self,age):
        return age
    
    

    def talk(self, message):
        print(message)

    def walk(self):
        print(f"{self.name} walking...")

human1= Human() #instance ürettik. istediğim noktada bir örnek oluşturmak istioyurm
human1.name= "ahmet"
human1.talk("hocam")
human1.walk()

#classımın içerisinde tanımladığım propertielerdir diye belirtmeme yardımcı oluyor.
#self olmasaydı o classa ait instance değerlere ulaşamıyoruz.
#fonksiyonların ilk para
#ismini yaşını değiştirip özellik atayabilirim.
        
#python da yapıcı bloğun adı init

"""FUNKCIJE
    -funkcija je blok koda koji se pokrece samo kada je pozvan;
    -mozemo proslediti podatke tj. parametre u funkciju;
    -funkcija moze da vrati podatke kao rezultat;
    -u Pythonu funkcija je definisana sa kljucnom recju def
    -funkcija se poziva pomocu njenog imena koje je praceno sa zagradama;
    -infoirmacije se unose u funkciju kao argumenti, koji se navode iza imena funkcije unutar zagrada. moze imati beskonacno argumenata koje je potrebno odvojiti zarezom;
    -termini parametar i argument cesto se koriste za istu stvar: informacije koje se prosledjuju funkciji;
    -iz perspektive PYTHON-a: 
        PARAMETAR JE PROMENLJIVA NAVEDENA UNUTAR ZAGRADA U DEFINISANJU FUNKCIJA
        ARGUMENT JE VREDNOST KOJA SE SALJE FUNKCIJI KADA SE FUNKCIJA POZOVE
    """
def imefunkcije():
    print("Funkcija koja nema ulazne niti izlazne vrednosti nego samo sluzi da nesto odstampa")
imefunkcije()

def mojafunkcija(ime): #parametar je (ime)
    print(ime+ " Spahovic") 
mojafunkcija("Resad") #argument je (Resad)
mojafunkcija("Maida")
mojafunkcija("Atija")

#podrazumevano, funkcija mora biti pozvana sa tacnim brojem argumenata. to znaci ako funkcija ocekuje 2 argumenta mora biti pozvana sa dva argumenta ni manje ni vise
def imeprezime(imen, prezime):
    print("Moje ime je "+imen+" a prezime je "+prezime)
imeprezime("Resad", "Spahovic")
imeprezime("Maida", "Spahovic")
#imeprezime("Resad") greska, jer ima manje argumenata
#imeprezime("Maida","Baltic", "Spahovic") greska, jer ima vise argumenata

#ukoliko ne znamo koliko cemo da preosledimo argumenata nasoj funkciji, dodajemo * ispred imena parametara u definisanju funkcije

def argumenti(*deca):
    print("Najmladje dijete je "+deca[2]+ " a najstarije nase dijete je: "+deca[0])
argumenti("Atija", "Adem", "Jusuf", "Uma")

def zbir(a, b, c):
    print(a+b+c)
zbir(10, 20, 30)

def kljuc(dete1, dete2, dete3):
    print("najmladje dijete je: "+dete3) #ne moramo da koristimo sve paramtre, mozemo samo odredjene, ali mora da bude jednak broj argumenata i parametara da se ne bi pojavila greska
    print("Nase najstarije dijete i nase mezimce je "+dete1)
kljuc(dete1="Atija", dete2="Adem", dete3="Uma") #mora da je isti broj parametara i argumenata

#ukoliko ne znamo koliko ce argumenata kljucne reci da bude prosledjeno nasoj funkciji dodajemo ** ispred imena parametara u definiciji funkcije
#na ovaj nacin funkcija ce dobiti recnik argumenata i moze pristupiti stavkama u skladu sa tim

def funkcija(**decaa):
    print("Nase najstarije dijete je: "+decaa["imedeteta"])
funkcija(imedeteta = "ATIJA", prezimedeteta = "Spahovic")

#podrazumijevana vrijednost parametara

def podrazumevano(drzava = "Srbija"):
    print("Ja sam iz drzave: "+drzava)
podrazumevano("Nemacka")
podrazumevano("Italija")
podrazumevano("Norveska")
podrazumevano() #poziva sa podrazumevanom vrednoscu kada se pozove bez argumenata
podrazumevano("BiH")

#lista kao argument - argumenti mogu biti brojevi, stringovi, nizovi, tuple...

def lista(niz): #parametar je niz
    for x in niz:
        print(x)
voce = ["jabuka", "kruska", "banana", "kivi"]
povrce = ("paradajiz", "paprika", "boranija", "cvekla")
boje = ["plava", "crvena", "crna"]
lista(voce)
lista(povrce)
lista(boje)

def liste(duzina):
    for x in duzina:
        if x == 11: #ne zelimo da stampamo i 11 zato print ide posle
            break
        print(x)

brojevi = range(15)
liste(brojevi)

#povratne vrijednosti

def zbirbrojeva(x, y):
    return x+y
print(zbirbrojeva(12, 12))
a = zbirbrojeva(10, 5)
print(a*5)

#prazna funkcija
def praznafunkcija():
    pass


def razlika(a,b):
   print(a-b)
razlika(10, 2)

def razlika2(ab, cd):
    return ab-cd
print(razlika2(10, 2))
print("----------------------")
#rekurzija
"""def rekurzija(k):
    if k>0:
       result = k + rekurzija(k - 1)
       print(result)
    else:
        result = 0
    return result
"""
#rekurzija(6)
print("----------------------")
def vracanje(v):  #10+9+8+7+6+5+4+3+2+ = 54, 9+8+7+6+5+4+3+2 = 44, 8+7+6+5+4+3+2 = 35 .... 3+2 = 5, 2 = 2.
    if v>1:
        nesto = v + vracanje(v - 1)
        print(nesto)
    else:
        nesto = 0
    return nesto
vracanje(10)

#lambda funkcije
#moze imati bilo koji broj argumenata ali moze imati samo jedan izraz

x = lambda a : a+100+a
print(x(2))

x = lambda a, b, c, d, e: a+b+c+d+e
print(x(2, 4, 5, 6, 7))

def funkcija(n):
    return lambda a: a*n

neka = funkcija(4)
print(neka(8))

def g(f):
    return lambda k: k*f

duplo = g(2)
troduplo = g(3)

print(duplo(11))
print(troduplo(11))

def paran(n):
    if n%2 == 0:
        print("Uneti broj je paran")
    else:
        print("Uneti broj je neparan")       
        
def pozitivan(a):
    if a>0:
        print("Uneti broj je pozitivan")
    else:
        print("Uneti broj je negativan.")

br = int(input("Unesite broj: "))
paran(br)
pozitivan(br)


#faktorijel
def fact(n):
    if n ==1: #ovo stavljamo da bi smo prekinuli for petlju nekada
        return 1
    return fact(n - 1)*n
print(fact(5))

def faktorijel(m):
    if m == 1:
        return 1   
    return faktorijel(m-1)*m
print(faktorijel(6))

a = lambda x : x * 10
print(a(10))

def lam(r):
    return lambda  y: y * r #pom = lambda y : y * 10

pom = lam(10)  
print(pom(10))

niz = ["maja", "atija", "resad", "adem"]
drugi = ["amra", "farah", "rajif", "jaman"]
drugi2 = ["amra", "farah", "rajif", "jaman", "resad", "maida", "atija", "adem"]

def stampa(nesto):
    for i in range(0,len(nesto)): #for i in nesto: print i
        print(nesto[i])
print(" ")
stampa(niz)
print(" ")
stampa(drugi)
print(" ")
stampa(drugi2)

a = []
def unos():
    #a =[], a ako hocemo da nam pamti rezultate onda ovo a stavljamo ispred def unos()
    while True:
        c = input("UNESITE IME: ").capitalize()
        if c == " ":
            break
        else:
            a.append(c)
    print(a)
print("PRVI NIZ JE: ")
unos()
print("DRUGI NIZ JE: ")
unos()




#nizovi
#python nema ugradjenu podrsku za nizove, ali se umesto njih koriste liste. sada pokazujemo kako koristimo liste kao nizove. 
#medjutim, da bi smo radili bas sa nizovima moramo da uvezemo biblioteku kao sto je biblioteka NumPy

auta = ["Ford", "Audi", "Volvo", "BMW", "Saab"]
print(auta)
for x in auta:
    print(x)
if "Ford" in auta:
    print("Postoji auto Ford u nizu auta. ", auta[0])
print(auta[0:3])
print(auta[:2])
print(auta[2:])
auta.insert(2, "Mercedes") #dodaje na drugom mestu bez zamene
print(auta)
auta[2] = "Jeep" #menja stavku na drugom mestu
print(auta)
auta.append("VW")
auta.append("Mustang")
print(auta)
print(len(auta))
auta.pop(2)
auta.pop()
auta.remove("Volvo")
print(auta)
auta.clear()
print(auta)
del auta

#KLASE I OBJEKTI
class prva: #da bi smo kreirali klasu koristimo kljucnu rijec class. sada pravimo klasu naziva prva sa vrednoscu sa imenom x
    x = 5
print(prva)

p1 = prva() #sada koristimo klasu pod nazivom prva za kreiranje objekata
print(p1.x)

"""Ovi primeri su klase i objekti u njihovom najednostaqvnijem obliku i nisu bas korisni u aplikacijama iz stvarnoga zivota
Da bi smo razumjeli znacenje klase, moramo razumjeti ugradjenu funkciju _init_()
Sve klase imaju funkciju koja se zove _init_() i koja se uvek izvrsava kada se klasa pokrece
"""
#Napravite klasu pod imenom osoba, koristite funkciju init da dodelite vrednost za ime, prezime i uzrast

class Osoba:
    def __init__(self, ime, godine):
        self.ime = ime
        self.godine = godine

o1 = Osoba("Resad", 29)
o2 = Osoba("Maida", 30)
o3 = Osoba("Atija", 2)

print(o1.ime, o1.godine)
print(o2.ime, o2.godine)
print(o3.ime, o3.godine)

class Auto:
    def __init__(self, marka, kubikaza):
        self.marka = marka
        self.kubikaza = kubikaza
a1 = Auto("BMW", 1990)
a2 = Auto("Audi", 2200)

print(a1.marka, a1.kubikaza)
print(a2.marka, a2.kubikaza)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

p1 = Person("John", 36)
p2 = Person("Altidor", 67)
p3 = Person("Mark", 32)
p4 = Person("Ross", 31)
print(p1)
print(p2.name, p2.age)
print(p3)
print(p4.age)

class Voce:
    def __init__(self, ime, boja, ukus):
        self.ime = ime
        self.boja = boja
        self.ukus = ukus
    def __str__(self):
        return f"{self.ime} {self.boja} {self.ukus}"
v1 = Voce("jabuka", "zelena", "kisela")        
v2 = Voce("ananas", "zuta", "sladak")
v3 = Voce("kivi", "zelena", "kiseli")
print(v1)
print(v2)
print(v3.ime, v3.ukus)
print(v2.boja)

#objekti takodje mogu sadrzati i metode. metode u objektima su funkcije koje pripadaju objektu

class Ljudi:
    def __init__(self, ime, godine):
        self.ime = ime
        self.godine = godine
    def funkcija(self):
        print("Moje ime je ",self.ime, " i imam ",self.godine," godina.")
    
lj1 = Ljudi("Resad", 29)
lj1.funkcija()

class Zbir:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def zb(self):
        print(self.x+self.y+self.z)
    
z1 = Zbir(3,4,5)
z1.zb()

class Proizvod:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def pro(self):
        return self.a*self.b*self.c*self.d
p5 = Proizvod(2,3,4,5)
print(p5.pro())

#NASLEDJIVANJE
#RODITELJSKA KLASA JE KLASA OD KOJE SE NASLEDJUJE, NAZIVA SE I BAZNA KLASA
#CHILD KLASA JE KLASA KOJA NASLEDJUJE DRUGU KLASU, NAZIVA SE I IZVEDENA KLASA
#svaka klasa moze biti roditeljska klasa tako da je sintaksa ista kao i za kreiranje bilo koje druge klase

class ImePrezime:
    def __init__(self, ime, prezime, god):
        self.ime = ime
        self.prezime = prezime
        self.god = god
    def odstampaj(self):
        print("Moje ime je",self.ime,"a prezime je",self.prezime,"i imam",self.god,"godina")

class Sin(ImePrezime):  #klasa sin je nasledila sve iz klase roditelja tj klase imeprezime
    pass

class Cerka(ImePrezime): #klasa cerka je nasledila sve iz klase roditelja tj klase imeprezime
    pass

class Atija(ImePrezime): #takodje nasledjuje sve iz klase roditelja
    def __init__(self, ime, prezime, god):
        ImePrezime.__init__(self, ime, prezime, god)

class Adem(ImePrezime):
    def __init__(self, ime, prezime, god): #koriscenjem funkcije super() ne moramo da koristimo ime roditeljskog elementa, automatski se nasledjuju metode i svojstva od svog roditelja
        super().__init__(ime, prezime, god)


ip1 = Sin("Resad", "Spahovic",29)
ip2 = Cerka("Maida", "Baltic",30)
ip3 = Atija("Atija", "Spahovic", 2)
ip1.odstampaj()
ip2.odstampaj()
ip3.odstampaj()

class Neko:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def zbir(self):
         print (self.a+self.b+self.c+self.d) #f se koristi kada se vrsi stampa teksta
n1 = Neko(2,4,5,6)    
n1.zbir()

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

voce = ("jabuka","banana","kruska","ananas","kivi") 
stavka = iter(voce)
print(next(stavka))
print(next(stavka))
print(next(stavka))
print(next(stavka))
print(next(stavka))

mystr = "banana"
for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 3
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Iteracija:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=3
        return x

itera = Iteracija()
mojiter = iter(itera)
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))
print(next(mojiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

class Pogon:
    def __init__(self, metraza, materijal):
        self.metraza = metraza
        self.materijal = materijal
    def ispis(self):
        print ("Koristimo metrazu",self.metraza,"kao i materijal",self.materijal,"koji je bas dobar i bas pogodan")
a = Pogon(1234, "pamuk")
a.ispis()

class Proizvod:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def pro(self):
        return self.a*self.b*self.c*self.d
p5 = Proizvod(2,3,4,5)
k = p5.pro()
print("Proizvod brojeva je",k)

class Tepisi:
    def __init__(self, kolekcije, dimenzija):
        self.kolekcije = kolekcije
        self.dimenzija = dimenzija
    def tepih(self):
        print("Tepih je kolekcije",self.kolekcije,"dimenzije",self.dimenzija,"cm.")
s = Tepisi("SARDES","160X230")
g = Tepisi("GASPARA", "200X300")

s.tepih()
g.tepih()

class Iter:
    def __init__(self, a, b):
        pass
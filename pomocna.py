def samostampa():
    print("Ovo je funkicja bez parametara i argumenata. Nema ulaznih niti izlaznih podataka. ova funkcija samo stampa")
samostampa()

def jedanparametar(ime):
    print("Moje ime je",ime,"a prezime je Spahovic")
jedanparametar("Resad")
jedanparametar("Maida")
jedanparametar("Atija")

def dvaparametra(ime, prezime):
    print("Moje ime je",ime,"a prezime je",prezime)
dvaparametra("Resad","Spahovic")
#dvaparametra("Maida")
#dvaparametra("Atija","Spahovic", 23)

def triparametra(ime, prezime, godine):
    print("Moje ime je",ime,"a prezime je",prezime)
triparametra("Resad","Spahovic", 29)

def nargumenata(*ime):
    print("Moje ime je",ime[3],"a prezime je Spahovic")
nargumenata("Resad", "Maida","Atija","Adem","Uma","Jusuf","Davud")

def kljucevi(otac, majka, sin, cerka):
    print("Ime oca je",otac,"ime majke je",majka,"ime sina je",sin,"ime cerke je",cerka)
kljucevi("Resad","Maida","Adem","Atija")
kljucevi(sin = "Adem", cerka="Atija", majka="Maida", otac="Resad")

def deca(**brdece):
    print("Nase najstarije dijete je",brdece["cerka"])
deca(sin="Adem", cerka="Atija", cerkica ="Uma")

voce = ["jabuka", "banana", "anans", "kivi"]
povrce = ("paradajiz", "paprika", "cvekla", "jabuka")

def niz(listup):
    for x in listup:
        if x == "jabuka":
            print(x)
niz(voce)
niz(povrce)

brojevi = range(10, 60, 2)

def rang(a):
    for x in a:
        print(x)
        if x == 18:
            break      
rang(brojevi)

def povratnavrednost():
    x = 10+20+30
    return x
print(povratnavrednost()) 

def povjedan(a,b,c):
    return a+b+c
a = povjedan(10,20,320)
print(a)

niz = range(0,101,1)
def suma(s):
    a=0
    for x in s:
        print(x)
        a = a+x
    print(a)
suma(niz)

def praznafunkcija(parametar):
    pass

def rek(rekurzija):
    if rekurzija>1:
        a = rekurzija+rek(rekurzija-1) #11+10+9+...+1= 65, 10+9+...+1 = 54, 9+8+...+1 = 44 ...
        print(a)
    else:
        a = 0
    return a
rek(11)

y = lambda a: a*a
print(y(3))

def funkcija(n):
   c = lambda a: a*n
   return c

k = funkcija(5)
print(k(10))
print(k(10))
print(k(20))

x = 7
y = 10.9
z = 2j
print(type(x))
print(type(y))
print(type(z))
A, B, C = "resad", "maida", "atija" #treba da se vodi racuna da su jednaki broj promenjivih i broj vrednosti koje dodeljujemo promenljivim
print(A)
print(B)
print(C)
X = Y = Z = "porodica"
print(X)
print(Y)
print(Z)

l = str(2)
print(type(l))
print(l)
k = "2"
print(type(k))
print(k)

print(bool(""))
print(bool())
print(bool([]))
print(bool(False))
print(bool(0))

print(bool("tacno"))
print(bool(-1123))
print(bool(True))
print(bool(["tacno","netacno"]))

print(bool())

def funkcija():
    return 0
print(bool(funkcija()))

vrednost3 = 123.3435
if isinstance(vrednost3, int): #ako je vreijednost celobrojna odradi if petlju
    print("data vrednost je celobrojna")
else:  #ako nije onda je napravi da jeste celobrojna i istampaj tekst kao i nju
    vrednost3 = int(vrednost3)
    print("Napravili smo celobrojnu vrijednost")
    print(vrednost3)

boje = ["crvena", "zelena", "zuta"]
voce = ["malina", "jabuka", "dunja"]

for x in boje:
    for y in voce:
        print(x,y)
import random
import sys
import os

# UNOS
print("--------VEZBE PAJTONA--------")
print("Sabirak 2+2 =",(1+2),end="")
print(" i to je prost broj.")
k = input("Unesi neki broj bezveze:")
duzina = len(k) #duzina reci

# LISTA
primer_liste1=['prvi_el','cetvrti_el','treci_el']
primer_liste1[1]="drugi_el"
print("Drugi element je:",primer_liste1[1])

primer_liste2=['pod1_el','pod3_el','pod4_el']
spoj_lista=[primer_liste1,primer_liste2]
print(spoj_lista)
print('Drugi element prve liste :',(spoj_lista[0][1]))

primer_liste1.append('cetvrti_el')#ubacivanje na kraj
primer_liste2.insert(1,'pod2_el')#ubacivanje gde ocu
print(spoj_lista)


# TUPLE?
tuple_primer=(3,2,4,5,1)
novi_tuple = list(tuple_primer)
nova_lista = tuple(novi_tuple)


# DICTIONARY
primer_dict={'Kole Pusac':'JJZ','Ivan Ljajic':'Pinki','Nikola Nikolic':'Svetina'}
print(primer_dict['Nikola Nikolic'])


# IF ELIF ELSE ,AND OR NOT
broj_1=3
if broj_1 > 4 :
    print("Broj_1 je veci od 4")
elif broj_1 == 3 :
    print("Broj_1 je jednak sa brojem 3")
else :
    print("Broj_1 je manji od 3")


# PETLJE(FOR,WHILE)
for x in range(0,5):
    print(x,' ',end="")
print("\n")

for y in primer_liste1:
    print(y)

for c in range(0,2):
    for d in range(0,2):
        print(spoj_lista[c][d])
i=0
while i != broj_1:
    print("Nije broj_1")
    i+=1


# FUNKCIJE
def saberi(br1,br2):
    sumBr=br1+br2
    return sumBr
print(saberi(broj_1,2))

# UNOS KORISNIKA
print("Koliko imas godina?")
godina=sys.stdin.readline()
god = int(godina)
if god >= 18:
    print("Punoletan si.")
else:
    print("Maloletan si")


# FILE
test_fajl=open("test.txt", "wb")
test_fajl.write(bytes("Neki tekst u fajlu \n",'UTF-8'))#unos teksta
test_fajl.close()

test_fajl=open("test.txt","r+")
tekst_fajla=test_fajl.read()
print(tekst_fajla)

#os.remove("test.txt")


# OBJEKTI
#Kada se prvi klasa potrebno je:__init__,set,get,toString
class Ucenik:
    _ime=""
    _godina=0
    _skola=""
    def __init__(self, ime, godina, skola):
        self._ime=ime
        self._godina=godina
        self._skola=skola
    
    def set_ime(self, ime):
        self._ime=ime
    def set_godina(self, godina):
        self._godina=godina
    def set_skola(self, skola):
        self._skola=skola

    def get_ime(self):
        return self._ime
    def get_godina(self):
        return self._godina
    def get_skola(self):
        return self._skola
    
    def get_tip(self):
        print("Ucenik")
    
    def toString(self):
        return "Ucenik {} ima {} godina i ide u {} skolu/gimnaziju".format(self._ime,self._godina,self._skola)

ucenik1 = Ucenik('Konstantin Pusac',18,'Jovinu')
print(ucenik1.toString())

class Mentor(Ucenik):
    _imeMentora = ""

    def __init__(self, ime, godina, skola, imeMentora):
        self._imeMentora=imeMentora
        super(Mentor, self).__init__(ime,godina,skola)

    def set_imeMentora(self, imeMentora):
        self._imeMentora=imeMentora

    def get_imeMentora(self):
        return self._imeMentora

    def get_tip(self):
        print("Mentor")

    def toString(self):
        return "Ucenik {} ima {} godina i ide u {} skolu/gimnaziju i njegov mentor je {} \n".format(self._ime,self._godina,self._skola,self._imeMentora)

mentor1= Mentor('Konstantin Pusac',18,'Jovinu','Zorana Babic')
print(mentor1.toString())

def vise_skola(self, koliko_puta=None):
    if koliko_puta is None:
        print(self.get_skola())
    else:
        print(self.get_skola()*koliko_puta)

class UcenikTest:
    def get_tip(self, ucenik):
        ucenik.get_tip()

test_ucenike=UcenikTest()

test_ucenike.get_tip(ucenik1)
test_ucenike.get_tip(mentor1)
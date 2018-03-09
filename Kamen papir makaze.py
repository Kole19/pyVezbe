lista_poteza=['kamen','papir','makaze']

# Komp
import random
for k in range(3):
  x = random.randint(0,3)
a = int(x)


# Korisnik
print(" 1 - kamen \n 2 - papir \n 3 - makaze")
y = input("Izaberite jedu od 3 opcije iznad \n")
b = int(y)

# Takmicenje
if a==1 and b==1:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[0],lista_poteza[0]))
    print("Izjednaceno je.\n")
elif a==1 and b==2:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[0],lista_poteza[1]))
    print("Pobedili ste.\n")
elif a==1 and b==3:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[0],lista_poteza[2]))
    print("Izgubili ste.\n")
elif a==2 and b==1:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[1],lista_poteza[0]))
    print("Izgubili ste.\n")
elif a==2 and b==2:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[1],lista_poteza[1]))
    print("Izjednaceno je.\n")
elif a==2 and b==3:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[1],lista_poteza[2]))
    print("Pobedili ste.\n")
elif a==3 and b==1:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[2],lista_poteza[0]))
    print("Pobedili ste.\n")
elif a==3 and b==2:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[2],lista_poteza[1]))
    print("Izgubili ste.\n")
elif a==3 and b==3:
    print("Komp: {}  Korisnik: {}".format(lista_poteza[2],lista_poteza[2]))
    print("Izjednaceno je.\n")
import random

def ispis_liste(lista):
    for x in range(0,duzina_reci):
        print(lista[x],end="")  

moguce_reci = ['stolica','kompijuter','monitr','kuciste','grafick']

x = random.randint(0,4)
rec = moguce_reci[x]
duzina_reci = len(rec)


#"Rec: ",
i=0
lista=[]
for x in range(0,duzina_reci):
    lista.append('_ ')

print(ispis_liste(lista))

while i != duzina_reci:
    slovo=input("Slovo: ")
    #slov=str(slovo)
    for x in range(0,duzina_reci):
        if slovo==rec[x]:
            lista.insert(x-1,slovo)
            i+=1
    print(ispis_liste(lista))
        

    



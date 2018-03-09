def prost_br(broj):
    dalije=0
    for x in range(2,broj):
        if broj%x is 0:
            dalije+=1
    if dalije >= 1:
        print("Broj nije prost.")
    else:
        print("Broj je prost.")
        

a = input("Unesi broj: ")
broj = int(a)

prost_br(broj)

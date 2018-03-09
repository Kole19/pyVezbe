def izborjKeceve(lista):
    n=0
    for x in lista:
        if(lista[x]==1):
            n=n+1
    return n
        

def countBits(n): 
    listaBr=['0']
    k=0
    while k!=0 or k!=1:
        k=n
        k=k%2
        n=n/2
        listaBr.append(k)
        return listaBr
        
listaBr=['0']
br= izborjKeceve(listaBr)
print(br)

            


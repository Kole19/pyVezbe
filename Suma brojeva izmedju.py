def veci_br(a,b):
    if a>b:
        return a
    else:
        return b
      
def manji_br(a,b):
    if a<b:
        return a
    else:
        return b

def get_sum(a,b):
    krajnje_res=0
    if a==b:
        return a
    else:
        x=veci_br(a,b)
        y=manji_br(a,b)
        kraj = x-y
        v=0
        while v!=kraj+1:
            krajnje_res+=y
            y+=1
            v+=1
    return krajnje_res

print(get_sum(1, 0)) 
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
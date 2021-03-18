from random import randint as roll

def rlist():
    while True:
        try:
            n=int(input("mege8os listas plz: \n"))
        except TypeError: print("me akeraio ari8mo to",end=' ')
        else :
            break
    lista=[]

    for i in range(n): lista.append(roll(1,6))

    return(lista)


def freq(lista):
    n=len(lista)
    for i in range(6):
        if(lista.count(i+1)):
            stars='*'
            stars*=lista.count(i+1)
            stars+='('+str(lista.count(i+1))+')'
            print(i+1,":"+stars)
    print("suxnotites: ")
    for i in range (6):print(i+1,':',lista.count(i+1)/n)
    
randlist=rlist()
print(randlist)
print(freq(randlist))

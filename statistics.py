from random import randint  as roll
from math import sqrt
                            #using mean value as a switch
def stats(lista,mesos=0):   #as to not unecessarrily call parts of the 
    if(mesos==0):           #function when not needed
        for i in range(len(lista)):
            mesos+=lista[i] 
        mesos/=len(lista)
        return mesos        #unsure whether I can return multiple values
    
    else :
        sd=0
        for i in range(len(lista)):
            sd+=(lista[i]-mesos)**2
        sd/=(len(lista)-1)
        sd=sqrt(sd)
        return sd           #unsure whether I can return multiple values
    
    
def main():
    lista=[]
    length=20
    for i in range(length):lista.append(roll(1,20))
    MO=stats(lista)
    SD=stats(lista,MO)
    print(f"\nThe list's mean is {MO} with a \n standart deviation of {SD}\n")


if __name__=="__main__":
    main()

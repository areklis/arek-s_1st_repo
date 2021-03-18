def powe(m,n):
    if (n==0): return 1
    elif (n>0) :
        return m*powe(m,n-1)
    else : return 1/(powe(m,-n))

m=float(input("\ndwse vasi\n"))
n=int(input("\ndwse ek8eti\n"))

print('\n',powe(m,n),'\n')

def factorial_2(n):
    if n<0:
        return 'Error: negative value'
    elif n==0:
        return 1
    else :
        return n*factorial(n-1)

def ann(i):
    if i>1 :
        return i*ann(i-1)
    else : return 1
k=int(input("\nparagontiko tou poso?\n"))
k=abs(k)
nn=1
for i in range(k):
    nn*=i+1

print("\nfor dinei:\n",nn,"\n")
nn=1
i=k
while (i>0):
    nn*=i
    i-=1

print ("\nwhile dinei:\n",nn,"\n")
print("\nanadromiki dinei:\n",ann(k))

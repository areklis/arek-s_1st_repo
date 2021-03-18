def randa_ola(n=328937):
    from random import randint as roll
    a=''
    for i in range(n):
        if roll(0,1)==1 : b=65
        else : b=97
        c=roll(1,26)
        c+=b
        a+=chr(c)
    return a

def main():
    try:
        ttt=open("textwall","x")
    except:
        ttt=open("textwall","w")
    ttt.write(randa_ola())
    ttt.close()

main()
    
    
        
    

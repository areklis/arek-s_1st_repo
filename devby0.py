def main():
    flag=0
    retis=float(input("diairetis plz: "))
    while not flag :
        flag=float(input("diairetaios plz: "))
        if not flag : print("mi midenikos o",end=' ')
    print("apotelesma einai:",retis/flag)

if __name__=="__main__":
    main()

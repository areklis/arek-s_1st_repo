def km2m():
    km=float(input('dwse taxutita'))
    if km<0.0 :             
            print('negatives kill me')
    else :
            while(km>120):
                print("that's too much!")
                km=int(input('dwse taxutita pali'))
            print(km,'xiliometra einai',km*0.621371,'milia')

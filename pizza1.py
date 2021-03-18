'''# aplo
num=int(input('Poses pitses 8es?'))
i=0
sm=0.0
while (i<num) :
    tem=5.0
    flg1=None
    flg2=None
    flg1=input("Extra bacon Y/N ? ")
    flg2=input("Extra Pepper Y/N ? ")
    if((flg1=='Y' or flg1=='y') and (flg2=='Y' or flg2=='y'):
       print("den ginetai kai ta 2 tautoxwna")
    elif(flg1=='Y' or flg1=='y'): tem+=5*0.3

    flg=input("Extra Pepper Y/N ? ")
    if(flg=='Y' or flg=='y') :tem+=5*0.2
    sm+=tem
    i+=1
print('teliko poso', sm)
'''
# sun8eto

num=int(input('Poses pitses 8es?'))
i=0
sm=0.0
pizzaprice=5.0
while (i<num) :
    tem=pizzaprice
    flg=None
    flg=input("Extra bacon Y/N ? ")
    if(flg=='Y' or flg=='y'): tem+=pizzaprice*0.3
    flg=None
    flg=input("Extra Pepper Y/N ? ")
    if(flg=='Y' or flg=='y') :tem+=pizzaprice*0.2
    sm+=tem
    i+=1
print('teliko poso', sm)

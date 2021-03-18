mikos=float(input("dwse mikos "))
platos=float(input("dwse platos "))
input("dwse va8os ")
print("plaka kanw :P\nto emvadon einai",platos*mikos)

kmh=float(input("dwse taxitita "))
mph=kmh*0.6214
if (kmh<0.0):print("pas me tin opis8en?")
elif(kmh>120.0):print("nomizw me",mph,"milia ana wra, pas ligaki upervolika grigora")
else:print("kala eisai")

#disekto
etos=int(input("xronologia? "))
if (etos%100!=0):
    if (etos%4==0):print("disekto!")
elif(etso%400==0):print("disekto!")


#calc
ope=str(input("ti praksi 8es na kaneis?\n(+,-,*,/)\n"))
nu1=float(input("dwse prwto noumero "))
nu2=float(input("dwse deutero noumero "))
if(ope=='+'):print("apotelesna pros8esis: ",nu1+nu2)
elif(ope=='-'):print("apotelesma afairesis: ",nu1-nu2)
elif(ope=='*'):print("apotelesma pollaplasiasmou: ",nu1*nu2)
elif(ope=='/'):print("apotelesma diairesis: ",nu1/nu2)
else:print("evales la8os telesti, praksi den egine")



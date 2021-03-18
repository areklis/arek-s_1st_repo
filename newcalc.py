def tst(a):
    

def calc():
    ope='0'
    while not (ope=='+' or ope=='-' or ope=='*' or ope=='/'):
        ope=str(input("ti praksi 8es na kaneis?\n(+,-,*,/)\n"))
    while True:
        try:
            nu1=float(input(" prwto noumero "))
        except ValueError:
            print(" prospa8ise ksana me ari8mitiko",end='')
            continue
        else:
            break
    while True:
        try:
            nu2=float(input("deutero noumero "))
        except ValueError:
            print(" prospa8ise ksana me ari8mitiko",end='')
            continue
        else:
            if (ope=='/' and nu2==0):
                print("mi mideniko ",end='')
                continue
            else: break
    if(ope=='+'):print("apotelesna pros8esis: ",nu1+nu2)
    elif(ope=='-'):print("apotelesma afairesis: ",nu1-nu2)
    elif(ope=='*'):print("apotelesma pollaplasiasmou: ",nu1*nu2)
    elif(ope=='/'):print("apotelesma diairesis: ",nu1/nu2)

calc()

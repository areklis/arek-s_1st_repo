def enq(fl1,que1,pos):
    if(pos==0):que1.insert(0,fl1)
    else:que1.append(fl1)
    return que1
def rem(que1,pos):
    if(pos==0):que1.remove(que1[0])
    else:que1.remove(len(que1)-1)
    return que1
#converting str to float
def digi(fl1):
    if fl1[0]=='-':fl1
    
def main():
    que=[]
    fl='paso' #setting our operations flag

    while(fl[0]!='q' and fl[0]!='Q'):
        fl=input("\nplease enter your input\n")
        if(fl[0]=='q' or fl[0]=='Q'):print("\nquitting...")
        elif(fl=='r'):que=rem(que,None)
        elif(fl=='0r'):que=rem(que,0)
        elif(fl[0]=='0'):
            fl=float(fl)
            que=enq(fl,que,0)
        else:
            fl=float(fl)
            que=enq(fl,que,None)
        print('\n',que,'\n')
        fl='paso'
if __name__=="__main__":
    main()

def caeser(a,key=3):
    b=''
    for i in range(len(a)):
        b+=chr(ord(a[i])+key)
    return b

def prntC(a):
    print('',a,'\n becomes\n',caeser(a))


prntC('CONFERENCE')

def conv():
    byte=input('give byte')
    dec=0
    for i in range(8):
        dec+=((byte[i]*2)**i)
    print (dec)
    return dec

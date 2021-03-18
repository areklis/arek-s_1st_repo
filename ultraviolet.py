uv=-1
#while(uv<0.0) :
while(uv<0 or uv>15):
    uv=float(input("eisigage timi deikti UV: "))
    if(uv<0.0 or uv>15):
             print("lan8asmeni timi, parakalw prospa8eiste ksana")
if(uv<6):
   print("elaxistos 'h mikros kundinos")
elif(uv<11):
    print("megalos-polu megalos kundinos")
#elif(uv<15):
else:
    print("akraia katastasi")
#else:
#    print("ksefigame teleiws")

name=input('\nHello <<unknown user>>\n plz make urself known:\n')
age='none'
while age.isdigit()==False :
    age=input("\nplease fill in your age in years:\nMake sure it is a positive number\n")
age=int(age)
#if (age<0):
#    print("very funny")
#    age=abs(age)

weight='none'
while weight.isnumeric()==False :
    weight=input("\nplease disclose your weight in kilograms:\nMake sure it is a positive number\n")
weight=float(weight)
#if (weight<0) :
#    print("lmao")
#    weight=abs(weight)
if  (age<18): color='White'
elif(age<25): color='Pink'
elif(age<36):color='Red'
elif(age<46):color='Green'
elif(age<56):color='Blue'
else: color='Black'

if  (weight<50):size='Small'
elif(weight<65):size='Medium'
elif(weight<80):size='Large'
else: size='X-large'

print("\n Hey", name , ",it is cool to be",age,"years old! You should buy a",color,size,"shirt")

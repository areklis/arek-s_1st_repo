def fb5(i):
    if (i+1)%5==0 : return ('Buzz')
    else :return("")
    
def modu(x,div):
    return x%div==0


for i in range(100):

    if ((i+1)%15)==0 :
        print('"FizzBuzz"!!!')
    elif ((i+1)%3==0) :
        print('"Fizz"')
    elif ((i+1)%5==0) :
        print('"Buzz"')
    else :
        print(i+1)


for i in range(100):

    if ((i+1)%3==0) :
        print('Fizz'+str(fb5(i)))
    elif ((i+1)%5==0) :
        print(str(fb5(i)))
    else :
        print(i+1)


for i in range(100):
    u=i+1
    if (modu(u,15)) :
        print('"FizzBuzz"!!!')
    elif (modu(u,3)) :
        print('"Fizz"')
    elif (modu(u,5)) :
        print('"Buzz"')
    else :
        print(u)

def stars(number_of_stars,ctr=30):
    answer=''
    for i in range(number_of_stars) :
        answer+='*'
    answer=answer.center(ctr)
    return answer

print(stars(1))
print(stars(3))
print(stars(5))

for i in range(1,30,2):
    print(stars(i,40))

for i in range(15):
    print('*')

for i in range(15):
    print('*',end='')
print('')

for i in range(15):
    print(end='*')
print('')
    
for i in range(0,10,3):
    print(i, end='*')
print('')
suma=0
for i in [1,2,3,4]:
    suma=suma+i
print(suma)

lista=[1,2,3,4.101,107.2,22]
mymax=0
for i in lista:
    if i>mymax : mymax=i
print(mymax)

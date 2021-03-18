def ginomeno(x,y):
	return x*y


# function
def ask_name():
    name=input('Poio einai to onoma sou? ')
    return name


print('To onoma einai:',ask_name())
myname=ask_name()
print(myname)

# procedure
def diafora(x,y):
    diaf=x-y
    print('Diafora=',diaf)

diafora(4,2)

# parametroi proka8orismenis timis
def dynami(x,y=2):
    return x**y

dyn=dynami(2)
print(dyn)
dyn=dynami(2,3)
print(dyn)

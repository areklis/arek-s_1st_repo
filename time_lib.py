from time import strftime, gmtime
print('Python shell has run off:',strftime("%a,%d-%b-%Y%H:%M",gmtime()))
print()
now=gmtime()
print(now)

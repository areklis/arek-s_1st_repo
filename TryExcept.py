try:
    print(x=None)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    dividend=float(input("Pleas ender the dividend: "))
    divisor=float(input("Please enter da divisor: "))
except: print("try inputting numburs next time")
try:
    quotient = dividend/divisor
except ZeroDivisionError: print("∞")
except : print("something went wrong the wrong way")
print(quotient)

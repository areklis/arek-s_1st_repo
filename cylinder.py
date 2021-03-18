from math import pi as pi
from math import pi as Pi

def volu(r,h): return pi*h*r**2

def SA(r,h): return 2*pi*r*(r+h)

def main():
    h=-1
    r=-1
    while h<0:
        h=float(input("please enter cylinter height:\n"))
        if(h<0):print("Negative value rejected.\n again, ", end='')
    while r<0:
        r=float(input("please enter cylinter radius:\n"))
        if(r<0):print("Negative value rejected.\n again, ", end='')
    print(f"Cylinder's volume is: {volu(r,h)},\nwhile\nits surface area is: {SA(r,h)}")

def cyli() :main()

if __name__=='__main__':
    main()

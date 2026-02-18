import math

def Areaoftriangle():
    a=float(input("Enter Side a: "))
    b=float(input("Enter Side b: "))
    c=float(input("Enter Side c: "))
    if a > 0 and b >0 and c >0 and a+b>c and a+c>b and b+c>a:
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"The area of the triangle is {area}.")
    else:
        print("A, B, and C must be positive numbers and satisfy the triangle inequity theorem, please press (ENTER) and enter positive numbers")
        Areaoftriangle()

def Areaofcylinder():
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    if r>=0 and h>=0:
        area= 2 * math.pi * r * (r + h)
        print(f"The area of the cylinder is {area}.")
    else:
        print("Radius and Height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        Areaofcylinder()

def Areaofsphere():
    r = float(input("Enter Radius: "))
    if r>=0:
        area = 4 * math.pi * r**2
        print(f"The area of the sphere is {area}.")
    else:
        print("Radius must not be a negative number, please press (ENTER) and enter a non-negative number")
        Areaofsphere()

def Areaofcircle():
    r = float(input("Enter Radius: "))
    if r>=0:
        area=math.pi * r**2
        print(f"The are of the circle is {area}.")
    else:
        print("Radius must not be a negative number, please press (ENTER) and enter a non-negative number")
        Areaofcircle()

def Areaofcuboid():
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    h = float(input("Enter height "))
    if l>=0 and w>=0 and h>=0:
        area= 2*(l*w + w*h + h*l)
        print(f"The are of the cuboid is {area}.")
    else:
        print("Length, width, and height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        Areaofcuboid()

def Areaofrectangle():
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    if l>0 and w>0:
        area= l * w
        print(f"The are of the rectangle is {area}.")
    else:
        print("Length and width must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        Areaofrectangle()

def Areaofcube():
    s = float(input("Enter Side: "))
    if s>=0:
        area= 6 * s**2
        print(f"The are of the cube is {area}.")
    else:
        print("Side must not be a negative number, please press (ENTER) and enter a non-negative number")
        Areaofcube()

def Areaofsquare():
    s = float(input("Enter Side: "))
    if s>=0:
        area= s**2
        print(f"The are of the square is {area}.")
    else:
        print("Side must not be a negative number, please press (ENTER) and enter a non-negative number")
        Areaofsquare()

def Areaofpyramid():
    b = float(input("Enter Base: "))
    w = float(input("Enter Width: "))
    s = float(input("Enter Side: "))
    if b>=0 and w>=0 and s>=0:
        ba= w * b
        la= 2 * (b*s+w*s)
        ta=la+ba
        print(f"The area of the pyramid is {ta}.")
    else:
        print("Base, width, and side must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        Areaofpyramid()

def Areaofcone():
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    if r>=0 and h>=0:
        s=math.sqrt(r**2+h**2)
        ba=math.pi * r**2
        la=math.pi*r*s
        ta=la+ba
        print(f"The area of the cone is {ta}.")
    else:
        print("Radius and height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        Areaofcone()

def Radiantodegree():
    ra=float(input("Enter Radian: "))
    if ra>= 0:
        de=math.degrees(ra)
        print(f"The degree conversion of {ra} radian-s is {de} degree-s.")
    else:
        print("Radian must not be negative, please press (ENTER) and enter a non-negative number")
        Radiantodegree()

def Degreetoradian():
    de=float(input("Enter Degree: "))
    if de>=0:
        ra=math.radians(de)
        print(f"The radian conversion of {de} degree-s is {ra} radian-s.")
    else:
        print("Degree must not be negative, please press (ENTER) and enter a non-negative number")
        Degreetoradian()

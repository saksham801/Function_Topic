# write a python program to calculate the area of a trapezoid
#1/2sum of length of parell side * height
def trapezoid():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    h = float(input("Enter the value of h: "))
    area = a+b
    area1 = area/2
    area2 = area1*h
    print("The area of the trapezoid is", area2)
    return area
#trapezoid()

# base * height
def parallegram():
    base = float(input("Enter the value of base: "))
    height = float(input("Enter the value of height: "))
    area = base*height
    print("The area of the parallegram is", area)
    return area
#parallegram()

def cylinder_volume():
    r = float(input("Enter the value of r: "))
    h = float(input("Enter the value of h: "))
    volume = 3.14*r**2*h
    print("The volume of the cylinder is", volume)
    return volume
#cylinder_volume()

def cylinder_curved_surface():
    r = float(input("Enter the value of r: "))
    h = float(input("Enter the value of h: "))
    curved = 2*3.14*r*h
    print("The volume of the cylinder curve is", curved)
    return curved
#cylinder_curved_surface()

def cylinder_surface_area():
    r = float(input("Enter the value of r: "))
    h = float(input("Enter the value of h: "))
    surface = 2*3.14*r*(r+h)
    print("The surface of the cylinder is", surface)
    return surface
#cylinder_surface_area()

def sphere_volume():
    r = float(input("Enter the value of r: "))
    volume = 4/3*3.14*r**3
    print("The volume of the sphere is", volume)
    return volume
sphere_volume()
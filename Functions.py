def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width

    print("The area of the rectangle is", area)


def volume_cube():
    length = float(input("Enter the length of the cube: "))
    width = float(input("Enter the width of the cube: "))
    height = float(input("Enter the height of the cube: "))

    volume = length*width*height

    print("The volume of the cube is", volume)


def area_circle():
    pi = 3.14
    radius = float(input("Enter the radius of the circle: "))

    area = pi*radius*radius

    print("The area of the circle is", area)


def circumference_circle():
    pi = 3.14
    radius = float(input("Enter the radius of the circle: "))

    circumference = 2*pi*radius

    print("The volume of the circle is", circumference)


def volume_sphere():
    pi = 3.14
    radius = float(input("Enter the radius of the sphere: "))

    volume = (4/3)*pi*radius*radius*radius

    print("The volume of the sphere is", volume)


while True:
    print("1. Calculate the area of a rectangle")
    print("2. Calculate the volume of a cube")
    print("3. Calculate the area of a circle")
    print("4. Calculate the circumference of a circle")
    print("5. Calculate the volume of a sphere")
    print("6. Exit program")

    Input = input("Enter selection: ")

    if Input == "1":
        area_rectangle()
    elif Input == "2":
        volume_cube()
    elif Input == "3":
        area_circle()
    elif Input == "4":
        circumference_circle()
    elif Input == "5":
        volume_sphere()
    elif Input == "6":
        print("Terminating program...")
        break

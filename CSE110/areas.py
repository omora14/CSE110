def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius", radius, "is", area_of_circle(radius))


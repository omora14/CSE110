# File: team03.py
# Author: Team 10

# Purpose: Write a program to compute the areas of three different shapes. Write strech challenge program too.

print()

square_length = input('Lenght of the square: ')
rectangle_width = input('Width of the rectangle: ')
rectangle_length = input('Length of the rectangle: ')
pi = 3.14
radius = input('Radius: ')

print()

print(f'What is the length of a side of a square? {square_length}')
print(f'The area of the square is: {float(square_length) ** (2)}')
print(f'What is the length of rectangle? {rectangle_length}')
print(f'What is the width of the rectangle? {rectangle_width}')
print(f'The area of the rectangle is: {float(rectangle_length) * float(rectangle_width)}')
print(f'What is the radius of the circle? {radius}')
print(f'The area of the circle is: {float(pi) * (float(radius) ** (2))}')

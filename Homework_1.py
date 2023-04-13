# Name: Donghyun Kim
# SBUID: 115338001
##################### SCORE ######################
####### Score:  0/10 

#################################################
# Remove the ellipses (...) when writing your solutions.
# you output: no valid output
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/troykim12/Homework_1.py"
# Put today's temperature in fahrenheit44
# Put your x1 -4
# Put your y1 -4
# Put your x2 -5
# Put your y2 5
# Put your x3 3
# Put your y3 -3
# Put your degree you want to calculate!23
# How many sides of a polygon?5
# How long is the length of a polygon?4
# Traceback (most recent call last):
#   File "d:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27\troykim12\Homework_1.py", line 117, in <module>
#     print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )
# NameError: name 'area' is not defined
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

fahrenheit = int(input("Put today's temperature in fahrenheit"))
def fahrenheit2celsius(fahrenheit): 
    celsius = (5/9)*(fahrenheit-32)
    return celsius
# This is a fruitful function
def what_to_wear(celsius):

    celsius = fahrenheit2celsius(fahrenheit)

    if celsius < -10:
        print("Please, wear a puffy jacket")
    
    elif celsius >= -10 and celsius < 0:
        print("Please, wear a scarf")
    
    elif celsius >= 0 and celsius < 10:
        print("Please, wear a sweater")

    elif celsius >= 10 and celsius < 20:
        print("Please, wear a light jacket")

    else:
        print("Please, wear a t-shirt")
# This is a void function

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  
x1 = int(input("Put your x1 "))
y1 = int(input("Put your y1 "))
x2 = int(input("Put your x2 "))
y2 = int(input("Put your y2 "))
x3 = int(input("Put your x3 "))
y3 = int(input("Put your y3 "))


def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs(((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2)

    return area

d1 = 0
d2 = 0
d3 = 0

def euclidean_distance(x1, y1, x2, y2):
    global d1
    global d2
    global d3
    d1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    d2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
    d3 = ((x1-x3)**2 + (y1-y3)**2)**0.5

    return d1, d2,d3

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    d1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    d2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
    d3 = ((x1-x3)**2 + (y1-y3)**2)**0.5

    P = d1 + d2 + d3

    return P



# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

deg = int(input("Put your degree you want to calculate!"))

def deg2rad(deg):
    rad = deg*(math.pi/180)

    return rad

number_sides = int(input("How many sides of a polygon?"))
length_side = int(input("How long is the length of a polygon?"))

def apothem(number_sides, length_side):
    apothem = length_side/2*math.tan(180/number_sides)

    return apothem

def polygon_area(number_sides, length_side):
    polygon_area = (number_sides*length_side*apothem(number_sides, length_side))/2

    return polygon_area
   


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# # Exercise 1 test
# fahrenheit = 40
# what_to_wear(fahrenheit2celsius(fahrenheit))

# # Exercise 2 test
# x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
# area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
# perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
# number_sides = 5
# length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))


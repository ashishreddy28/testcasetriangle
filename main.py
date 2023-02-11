import unittest
import math

print(" Hello this is Ashish Yeruva, this is my python code for triangle test case...")
a = input("Enter length of side A : ")
b = input("Enter length of side B : ")
c = input("Enter length of side C : ")

def classify_triangle():

    if a == b == c:
        print("The triangle is equilateral")
    elif a == b or b==c or c==a:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")

classify_triangle()


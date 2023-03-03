from math import sqrt
def distance():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    c_kvadrat = a ** 2 + b ** 2
    c = sqrt(c_kvadrat)
    print(c)
distance()

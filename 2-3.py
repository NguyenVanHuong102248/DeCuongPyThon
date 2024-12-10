import math

a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
if delta < 0:
    print("VN")
elif delta == 0:
    x = -b / (2*a)
    print("x = {}".format(x))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 = {}, x2 = {}".format(x1, x2))
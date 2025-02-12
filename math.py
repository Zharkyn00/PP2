#1
import math

d = int(input())
r = d * (math.pi / 180)
print(f"Output radian: {r:.6f}")

#2
h = int(input())
f_v = int(input())
s_v = int(input())
a = 0.5 * (f_v + s_v) * h
print(f"Expected Output: {a}")

#3
import math
n_s = int(input())
s_l = int(input())
a = (n_s * s_l ** 2) / (4 * math.tan(math.pi / n_s))
print(f"The area of the polygon is: {a}")

#4

l = int(input("input the length: "))
h = int(input("input the height: "))

s = float(l * h)
print(s)


from math import ceil, floor, trunc

a = 4.3
b = 4.5
c = 4.7

d = -4.3
e = -4.5
f = -4.7

# trunc()
print(trunc(a), trunc(b), trunc(c))
print(trunc(d), trunc(e), trunc(f))
print("\n")
# floor()
print(floor(a), floor(b), floor(c))
print(floor(d), floor(e), floor(f))
print("\n")
# ceil()
print(ceil(a), ceil(b), ceil(c))
print(ceil(d), ceil(e), ceil(f))
print("\n")
# int()
print(int(a), int(b), int(c))
print(int(d), int(e), int(f))
print("\n")

# round()
print(round(a), round(b), round(c))
print(round(d), round(e), round(f))

x = 18.2
print(round(x, -1))
print(round(5, -1))

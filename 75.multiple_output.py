def multiple_output(a,b):
    add = a+b
    subs = a-b
    mult = a*b
    return add, subs, mult

# print(multiple_output(5,2))

a = multiple_output(5,2)
x, y, z = multiple_output(5,2)

print(a)
print(x,y,z)

print(x)
print(y)
print(z)
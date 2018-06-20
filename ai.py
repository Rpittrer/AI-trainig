import sys as sys

print('hello world!')

a = 12
b = 24
c = a + b
print(a)
print(type(a))
print(sys.getsizeof(a))

squares = []

for x in range(1,10):
    squares.append(x**2)

print(squares)    

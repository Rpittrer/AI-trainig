import sys as sys

# print('hello world!')

# a = 12
# b = 24
# c = a + b
# print(a)
# print(type(a))
# print(sys.getsizeof(a))

squares = []

# for x in range(1,10):
#     squares.append(x**2)

# s = sum(squares)
# print(s)

# for x in squares:
#     print(x)

squares = [x**2 for x in range(11, 1, -1)]
print(squares)
finishers = [1, 'bob', 'ada', 'bea', 4]
print(finishers)

#age = input("How old are you? ")
#new  = [x**2 for x in finishers if type(x) == int]
#print(new)
#age = int(age)


def fun(arg):
    new = [x**2 for x in arg if type(x) == int]
    return new


abc = fun(finishers)
print(abc)

def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

# Make three pizzas with different toppings.
make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers',
 'onions', 'extra cheese')
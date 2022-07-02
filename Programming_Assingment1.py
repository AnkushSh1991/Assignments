# Programming Assignment -1 02072022


# 1. Write a Python program to print "Hello Python"?


print('Hello Python')
        # OR
def print_Hi(name):
    print(f'Hello {name}')


print_Hi('Python')


# 2. Write a Python program to do arithmetical operations addition and division ?

def math_operation(operator, a, b):
    match operator:
        case '+':
            return a + b
        case '*':
            return a * b
        case '-':
            return a - b
        case '/':
            return a / b
        case default:
            return "Not a valid arithmetical operator"


print(math_operation('+', 10, 5))
print(math_operation('*', 10, 5))
print(math_operation('-', 10, 5))
print(math_operation('/', 10, 5))

# 3. Write a Python program to find the area of a triangle ?
import math
def Area_Triangle(a, b, c):
   s=(a+b+c)/2
   return math.sqrt(s*(s-a)*(s-b)*(s-c))

print(Area_Triangle(12,5,13))

# 4. Write a Python program to swap two variables?

def swap_variables(a, b):
   t=a;
   a=b;
   b=t;
   print(f'swapped values are a {a} and b {b}')

print(swap_variables(10,20))

# 5. Write a Python program to generate a random number?

import random
print(random.random())




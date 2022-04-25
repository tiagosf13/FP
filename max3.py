# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with conditional statements (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input ("number?"))

# Use conditional statements instead of max function!
if x1>x2:
    if x1>x3:
        print (x1)
    else:
        print (x3)
elif x2>x3:
    print (x2)
else:
    print (x3)



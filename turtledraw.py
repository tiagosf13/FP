# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here

file = input("File?")

fileread = open(file)

while True:
    line = fileread.readline()
    line.strip()
    if (line == "UP"):
        t.up()
    elif (line == "DOWN"):
        t.down
    else:
        n = line.split()
        x = float(n[0])
        y = float(n[1])
        t.goto(x, y)
# wait
turtle.Screen().exitonclick()


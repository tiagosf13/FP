x1 = float(input("number? "))
x2 = float(input("number? "))

def maximo(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2
print ("{:.0f}".format(maximo(x1,x2)))


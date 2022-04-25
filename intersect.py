def intersects(a1, b1, a2, b2):
    if ((((a2 < b1) and (b2 > a1)) or ((a1 < b2) and (a2 < a1))) or ((a1 == a2))):
        Intersect = "True"
    else:
        Intersect = "False"
    return (Intersect)

def main():
    a1 = float(input("Insira o valor de A1:\n"))
    b1 = float(input("Insira o valor de B1:\n"))
    a2 = float(input("Insira o valor de A2:\n"))
    b2 = float(input("Insira o valor de B2:\n"))
    print (intersects(a1, b1, a2, b2))
main()
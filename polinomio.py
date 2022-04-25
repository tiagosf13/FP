#Lista de valores que o x toma

def polinomio(x):
    p = ((x**2)+(2*x)+3)
    return (p)

lista = [0, 1, 2, polinomio(1)]
lista2 = []
def main():
    for n in lista:
        lista2.append(polinomio(n))
    print (lista2)

main()
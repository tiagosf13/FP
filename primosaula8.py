def primesUpTo(n):
    listanumeros=[numero for numero in range(2,n+1)]
    listaprimos=[]
    listapossibilidades=[]
    for elemento1 in listanumeros:
        if elemento1**2 in listanumeros:
            listanumeros.pop(listanumeros.index(elemento1**2))
        for elemento2 in listanumeros:
            if elemento1==elemento2:
                continue
            else:
                listapossibilidades.append((elemento1,elemento2))
    print(listapossibilidades)
    for elemento in listapossibilidades:
        print(elemento[1])
        if elemento[0]%elemento[1]==0:
            listanumeros.pop(listanumeros.index(elemento[0]))
        elif elemento[1]%elemento[0]==0:
            listanumeros.pop(listanumeros.index(elemento[1]))
        else:
            continue
        print(listanumeros)

    return listanumeros


def main():
    n = int(input("Insira o número:\n"))
    print("Lista de primos",primesUpTo(n))

main()
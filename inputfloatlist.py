
# ESTE PROGRAMA CONTEM VARIOS EXERCICIOS (3A, 3B, 3C), SENDO QUE O 3C NAO FICOU COMPLETO, TENDO UM ERRO NAO PERCETIVAL NA EXECUÇÃO



#FUNCAO QUE CRIA UMA LISTA COM OS NUMEROS QUE O UTILIZADOR INSERE
def inputFloatList():
    lista = []
    print("Insira os números que pretende adicionar á lista:\n")
    while (input != ""):
        numeros = input()
        if (numeros == ""):
            break
        else: 
            numeros = float(numeros)
        lista.append(numeros)
    print("Lista:\n", lista)
    return (lista)

#FUNCAO QUE CONTA SE O ELEMENTO E INFERIOR AO VALOR A INSERIDO PELO UTILIZADOR
def countLower (lst,v):
    novalista = []
    for n in lst:
        if (n<v):
            novalista.append(n)
    print ("Lista com valores inferiores a v:\n", novalista)

def minmax(lst):
    print (lst)
    anterior = 0
    min = lst [0]
    max = 0
    for n in lst:
        if (n <anterior):
            min = n
        else:
          del(lst[n])
          print (lst)
          minmax(lst)
    print("Minimo: ", min)
    print ("Máximo: ", max)



# FUNCAO PRINCIPAL
def main():
    numver = float(input("Insira o valor de v:\n"))
    lista = inputFloatList()
    countLower(lista,numver)
    minmax(lista)
main()
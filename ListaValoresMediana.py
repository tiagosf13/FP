from xml.dom.expatbuilder import ElementInfo


def paridade(lst):
    if len(lst)%2 != 0:
        mediana = int((len(lst)/2)+0.5)
        #print("Len:", len(lst))
        #print("elemento",lst.index(lst[mediana]))
        return(lst[mediana])
    else:
        mediana = int((len(lst)/2))
        elementleft=int(mediana-1)
        elementright=int(mediana)
        #print("Len:", len(lst))
        #print("left",lst[elementleft],"right",lst[elementright])
        return(lst[elementleft],lst[elementright])

def main():
    #elementolista = 0
    listainput = []
    print("Insira os valores para a lista:\n")
    while True:
        valoresInput=input("")
        if valoresInput=="":
            break
        else:
            listainput.append(valoresInput)
    
    lista=sorted(listainput)
    print(paridade(sorted(lista)))
    print(sorted(lista))
    """print("Insira os valores a serem acrescentados na lista:\n")
    while elementolista != (""):
        elementolista = float(input())
        lista.append(elementolista)
    print(lista)"""

main()
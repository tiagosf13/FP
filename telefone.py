# Complete este programa como pedido no guião da aula.

def listContacts(contactos, morada_contactos):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^25} : {:<25}".format("Numero", "Nome", "Morada"))
    for num in contactos:
        if contactos[num] not in morada_contactos:
            morada_contactos.setdefault(contactos[num], '')
        print("{:>12s} : {:^25} : {:<25}".format(num, contactos[num], morada_contactos[contactos[num]]))

def filterPartName(contacts: dict, partName: str):
    newDict = {}
    for contact in contacts:
        nome = contacts[contact]
        if partName in nome:
            newDict[contact] = nome
    return newDict



def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("Associar (M)orada")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau",
        }

    morada_contactos={
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos, morada_contactos)
        elif op == "A":
            numero = input("Insira o numero que deseja adicionar:\n")
            nome = input("Insira o nome que deseja adicionar:\n")
            contactos.setdefault(numero, nome)
        elif op == "R":
            numero = input("Insira o numero que deseja procurar:\n")
            contactos.pop(numero)
            print(contactos)
        elif op == "N":
            numero = input("Insira o numero que deseja procurar:\n")
            if numero in contactos:
                print(contactos[numero])
            else:
                print(numero)
        elif op== "P":
            pesquisa = input('Introduz o nome que pretendes procurar: ')
            partDict = filterPartName(contactos, pesquisa)
            print('Contactos com "{}":'.format(pesquisa))
            listContacts(partDict)
        elif op== "M":
            numero = input("Insira o numero que deseja procurar:\n")
            if numero in contactos:
                print(contactos[numero])
                morada = input('Insira a morada a ser associada:\n')
                morada_contactos[contactos[numero]]=morada
                print('Morada Associada')
            else:
                print(numero)

        else:
            print("Não implementado!")
    

# O programa começa aqui
main()


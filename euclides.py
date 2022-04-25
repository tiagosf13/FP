def mdc(a,b):
    r = (a%b)
    if (r == 0):
        valor = b
    elif (r < 0):
        valor = "Não existe"
    else:   
        valor = mdc(b,r)
    return (valor)

def main():
    a = float(input("Insira o valor de A:\n"))
    b = float(input("Insira o valor de B:\n"))
    print("MDC:","{:.0f}".format(mdc(a,b)))
main()
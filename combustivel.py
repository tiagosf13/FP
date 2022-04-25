litros = float(input("Insira a quantidade de litros abastecidos:\n"))
preco = (litros*1.4)
if (litros>40):
    preco = (preco*0.9)
    print ("O valor a pagar é", preco)
else:
    print ("O valor a pagar é", preco)

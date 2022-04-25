def Tax(r):
    if (r <= 1000):
        Tax = (0.1*r)
    elif (r <= 2000):
        Tax = (0.2*r-100)
    else:
        Tax = (0.3*r-300)
    return (Tax)

def main():
    r = float(input("Insira o valor de r:\n"))
    print("tax(r) =", Tax(r))
   
main()
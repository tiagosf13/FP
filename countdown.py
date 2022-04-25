def countdown(N):
    while (N != 1):
        N = N-1
        print (N)
    return ("0")

def main():
    N = int(input("Insira o número para o qual a contagem deva começar:\n"))
    print(countdown(N))


main()
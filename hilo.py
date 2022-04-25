# Complete the code to make the HiLo game...

import random

secret = random.randrange(1, 101) # Escolhe um numero random
def main():
    print(secret)
    print("Can you guess my secret?\n")
    guess = int(input("Insira um número:\n")) # Insere o numero
    while (guess != secret):
        
        if (guess > secret):
            print ('High')
            main()
        elif (guess < secret):
            print('Low')
            main()
        else:
            break
    print ('Correto')
main()
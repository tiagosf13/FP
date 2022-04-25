import random

secret = random.randrange(1, 101) # Escolhe um numero random

n=0
count = 0
while n!=secret :
    print (secret)
    n= int(input('Insira um número: '))
    if n>secret :
        print ('High')
        count += 1
    elif n<secret: 
        print('Low')
        count += 1
print ('Correto')
print ("Tentativas =", count)


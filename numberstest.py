number = [10,9,8,7,6,5,4,3,2,1,0]
newordernumber = []
print(number[0:9:2])
for i in range(len(number)):
    newordernumber.append(i)
    print (i, number[i])
print('')
print(newordernumber)   
for i, f in enumerate(number):
    print(i,f)

s2 = 0
x = 5
s2+=len(x.rstrip())
print(s2)
print(range(4))
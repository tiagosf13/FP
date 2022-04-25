s = 0
for m in range(4,-1,-1):
    x = (-1)**(m)*(2**m)
    s += x
    if m%2 != 1:
        print(x, end="")
    else:
        print (x, end="+")
else:
    print ("=", s, sep="")
print("Value x:", x)
print("Value m:", m)
print("Value s:", s)
print("abc".upper()*2)



x = 10
y = 0

if x > 0 and y > 0:
    print('xyz')
else:
    print('xpto')

if x + y < 0:
    if x > y:
        print('xy')
    else:
        print('yx')
elif x == 0 or y == 0:
    if x == 0:
        print( y )
    else:
        print(x)
else:
    print('zz')



lstA = [1, 2, 3, 4, 5]
lstB = [6, 7, 8, 9, 10]
print(lstA[-2])
print(lstA[2]+lstB[1])
print(len(3*lstA))
lstC = 2*lstA[1::3] + lstB[:2]
for i in lstC:
    print(i, end=',')
print()

lst = ["alfa", "beta", "carl", "diego", "eva", "fiona"]
print (lst[2])



lstN = [1, 2,range(5), 3, 4, 5, 6]
print(lstN[2][3])

for n in range(5):
    print (n)
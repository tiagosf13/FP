from mailbox import NotEmptyError


with open("names.txt") as names:
    dicnomes = {}
    for lines in names:
        partsname = (lines.split())
        dicnomes.setdefault(partsname[0],partsname[-1])
    names.close()
    dicapelidos= {a : n for n,a in dicnomes.items()}
    print(dicapelidos)

print ("----------------------------------------------")
newlist=[]
with open("names.txt") as file:
    for line in file:
        newline=line.strip().split()
        newlist.append(newline)

newdic={}

for element in newlist:
    newdic.setdefault(element[0],element[1:])
print(newdic)

newdic["Nome"]= "Apelido"

for element in newdic:
    sobrenome =""
    for apelido in newdic[element]:
        if apelido=="Apelido":
            continue
        else:
            sobrenome += " "+apelido
    print("{:^20s}:{:<20s}".format(element, sobrenome))
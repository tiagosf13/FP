import sys
fileread = open(sys.argv[1], encoding="UTF-8")
file = sys.argv[1]

for n in fileread:
    line = fileread.readline()
    line = line.strip()
    line = line.lower()
    print (line)
    count ={}
    for p in line:
        if p.isalpha:

print(count)
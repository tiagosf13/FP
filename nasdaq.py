def main():
    fname="nasdaq.csv"
    lst=[]
    with open(fname) as file:
        for line in file:
            lst+=[line.strip().split("\t")]
        lst=sorted(lst, key=lambda element: (element[0],element[1]))
        for element in lst:
            print("{:^20} {:^20} {:>20} {:>20} {:>20} {:>20} {:>20}".format(element[0],element[1],element[2],element[3],element[4],element[5],element[6]))
main()
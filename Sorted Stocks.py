def sort(stocks):
   lst=(sorted(stocks, key=lambda elemento: elemento[0]))
   print("{:^20} {:<20} {:^20} {:^20} {:>20}".format("EMPRESA","CIDADE","VALOR DE ABERTURA","VALOR DE FECHO","VALORIZAÇÃO"))
   print("---------------------------------------------------------------------------------------------------------------")
   for element in lst:
       print("{:^20} {:<20} {:^20} {:^20} {:>20}".format(element[0],element[1],element[2],element[3], element[4]))


def main():
    stocks=[('INTC', 'Tokyo', 33.22001, 34.28999, 4509110), 
        ('EA', 'Paris', 72.63, 68.98, 1189510), 
        ('TSLA', 'Paris', 217.35, 217.75, 252500), 
        ('INTC', 'London', 34.249, 34.451, 1792860), 
        ('TSLA', 'London', 221.33, 229.63, 398520), 
        ('ATML', 'Frankfurt', 8.23, 8.36, 810440)]
    sort(stocks)


main()


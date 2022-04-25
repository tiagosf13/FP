def sorted(stocks):
   print(sorted(stocks, key=lambda elemento: elemento[0]))
   


def main():
    stocks=[('INTC', 'Tokyo', 33.22001, 34.28999, 4509110), 
        ('EA', 'Paris', 72.63, 68.98, 1189510), 
        ('TSLA', 'Paris', 217.35, 217.75, 252500), 
        ('INTC', 'London', 34.249, 34.451, 1792860), 
        ('TSLA', 'London', 221.33, 229.63, 398520), 
        ('ATML', 'Frankfurt', 8.23, 8.36, 810440)]
    sorted(stocks)


main()


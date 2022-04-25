
# This function checks if year is a leap year.
def isLeapYear(year):
    if (year%100 == 0):
        return (False)
    else:
        return (year%4 == 0)

# This function checks how many days the month has
def monthDays(year, month):
    if (isLeapYear(year) == True) and (month == 2):
        days = 29
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # This tuple contains the days in each month (on a common year)
        days = MONTHDAYS[month]
    return days

# Função definida para analisar se o mês tem 30 ou 31 dias, exceto o mês de Fevereiro, que passa a ser incluido na primeira condição da função monthDays
def paridade(month): 
    if ((month%2)!=0) or (month == 8):
        return ("False") 
    else:
        return ((month%2 == 0))

# This is wrong, too.
def nextDay(year, month, day):
    if (monthDays(year, month) == day) and (month == 12): # Caso em que mudamos de mes, ano e dia
        month = 1
        year += 1
        day = 1
    elif (isLeapYear(year) == True) and (month == 2) and (day == 29): # Caso em que é um ano bissexto e que o mês é fevereiro e o dia é 29
        month = 3
        day = 1
    elif (isLeapYear(year) != True) and (paridade(month) == True) and (day == 28): # Caso em que nao e um ano bissexto e que o mes e par e o dia e 28
        month = 3
        day = 1
    elif (paridade(month) != True) and (day == 31): # Caso em que o mes e impar e o dia e 31
        month += 1
        day = 1
    elif (paridade(month) == True) and (day == 30): # Caso em que o mes e par e o dia e 30
        month += 1
        day = 1
    else:
        day += 1
    return year, month, day


# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()

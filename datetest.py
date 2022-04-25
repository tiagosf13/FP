
# This function checks if year is a leap year.
# It is wrong: 1900 was a common year!
def isLeapYear(year):
    if (year%100 == 0):
        return ("False")
    else:
        return (year%4 == 0)

# This function has a semantic error: February in a leap year should return 29!
# Correct it.
def monthDays(year, month):
    if (isLeapYear(year) == True) and (month == 2):
        days = 29
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # This tuple contains the days in each month (on a common year).
        # For example: MONTHDAYS[3] is the number of days in March.
        days = MONTHDAYS[month]
    return days

def paridade(month): # Isto assume que agosto tem apenas 30 dias, apesar de ter 31, pois o mes de agosto é par, sendo um exceção ao longo do ano
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
    elif (isLeapYear(year) != True) and (monthDays(year, month) == 28): # Caso em que nao e um ano bissexto e que o mes e par e o dia e 28
        month = 3
        day = 1
    elif (monthDays(year, month) == 31): # Caso em que o mes é impar e o dia e 31
        month += 1
        day = 1
    elif (monthDays(year, month) == 30): # Caso em que o mes é par
        month += 1
        day = 1
    else:
        day += 1
    return year, month, day


# This is the main function
def main():
    ano = int(input("Insira o ano:\n"))
    mes = int(input("Insira o mês:\n"))
    dia = int(input("Insira o dia:\n"))

    print("Was", ano, "a leap year?", isLeapYear(ano))  
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("Teste______","January 2017 had", monthDays(ano, mes), "days")
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(ano, mes, dia)
    print(y, m, d)
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
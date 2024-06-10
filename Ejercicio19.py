#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by , but not on a century unless it is divisible by.

#How many Sundays fell on the first of the month between two dates(both inclusive)?

#Input Format

#The first line contains an integer, i.e., number of test cases.
#Each testcase will contain two lines on first line denoting starting date. on second line denoting ending date. 

def daysInMonth(month, year):
    month31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
    month30 = ['Sep', 'Apr', 'Jun', 'Nov']
    month28 = ['Feb']

    if month in month31:
        return 31
    elif month in month30:
        return 30
    elif month in month28:
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28

def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    years = list(range(1900, 2001))

    listDayPassed = []
    listFirstMonthDays = []

    current_day_index = 0  # Índice del primer día de la semana: Monday (0), Tuesday (1), ..., Sunday (6)

    for year in years:
        for month in months:
            for day in range(1, daysInMonth(month, year) + 1):
                if day == 1:
                    listFirstMonthDays.append(days[current_day_index])
                listDayPassed.append(days[current_day_index])
                current_day_index = (current_day_index + 1) % 7

    count = listFirstMonthDays.count('Sunday')
    print(count)#El numero total de veces que el primer dia de un mes fue un domingo en ese perido de tiempo
    print(len(listDayPassed))# Almacena todos los dias de la semana (Esto incluye todos los dias de todos los meses y años cubiertos por el rango)
    print('El dia es',day, 'del mes',month,'del año', year) #Imprime el dia, mes y año


main()

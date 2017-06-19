# Program: seconds.py
# Description: Convertir un número entero de segundos a años/meses/días/horas/minutos/segundos
# Author: Juan Pablo Trejos Rodriguez

result_str = "{} seconds are equivalent to {} years, {} months, {} days, {} hours, {} minutes and {} seconds"

def convert_seconds(seconds):
    """ (number) -> (number, number, number, number, number, number)
    return how many years, months, days, hours, minutes and seconds from a number of seconds
    """
    # TODO: calculate and return the correct values
    secs = seconds % 60
    seconds = seconds // 60
    minutes = seconds % 60 
    seconds = seconds // 60
    hours = seconds % 24
    seconds = seconds // 24
    days =seconds % 30
    seconds =seconds // 30
    months = seconds % 12
    seconds = seconds // 12
    years = seconds 

    totalfecha = (years, months, days, hours, minutes,secs)

    return totalfecha

def main():
    """ Main Program """
    seconds = int(input("number of seconds: "))
    (years, months, days, hours, minutes, secs) = convert_seconds(seconds)
    print(result_str.format(seconds, years, months, days, hours, minutes, secs))

if __name__ == "__main__":
    main()


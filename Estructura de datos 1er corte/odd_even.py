# Program: odd_even.py
# Description: Separar números pares y no pares en una lista y luego dar ambas listas
# Author: Juan Pablo Trejos Rodriguez

def odd_even(numbers):
    """ (list) -> (list, list)
    return two lists with odd and even numbers from a list of integer numbers
    """
    # TODO: calculate and return the correct lists
    
    numbers = list(numbers)
    
    print (numbers)
    #numbers = numbers.split()
    #numbers = list(numbers.split(" "))
    
    lista_pares = []
    lista_impares = []

    
    jj = (len(numbers))

    for i in range(jj):
        if (int(numbers[i])) % 2 == 0:
            lista_pares.append(numbers[i])   
        else:
             lista_impares.append(numbers[i])      
        
    
    return lista_impares, lista_pares

def main():
    """ Main Program """
    numbers= ((input("enter a list of numbers (separated by spaces): ")).split())
    # TODO: convert the string "1 2 3 4 5" into a list [1, 2, 3, 4, 5]
    (odds, evens) = odd_even(numbers)
    print("{} = {} and {}".format(numbers, odds, evens))

if __name__ == "__main__":
    main()



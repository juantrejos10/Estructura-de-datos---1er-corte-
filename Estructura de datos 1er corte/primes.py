# Program: primes.py
# Description: Separar números primos y no primos en una lista y luego tener ambas listas 
# Author: Juan Pablo Trejos Rodriguez 
def es_primo(num):
    if num<=1:
        
        return False
    else:
        for i in range(2,num-1):
            if num%i==0:
                
                return False

    if num%1==0 and num%num==0:
        
        return True

def primees(numbers):
    
    
    numbers = list(numbers)
    
    list_pri = []
    list_nopri = []

    
    jj = (len(numbers))

    for i in range(jj):
        if (es_primo(int(numbers[i])) == False):
            list_nopri.append(numbers[i])   
        else:
             list_pri.append(numbers[i])      
           
    return list_nopri, list_pri

def main():
    """ Main Program """
    numbers= ((input("enter a list of numbers (separated by spaces): ")).split())
    # TODO: convert the string "1 2 3 4 5" into a list [1, 2, 3, 4, 5]
    (pri, nopri) = primes(numbers)
    print("{} = {} and {}".format(numbers, pri, nopri))

if __name__ == "__main__":
    main()
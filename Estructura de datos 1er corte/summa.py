# Program: odd_even.py
# Description: Calcular la sumatoriade una funcion f(x) para valores entre a y b
# Author: Juan Pablo Trejos Rodriguez 
a = int(input("ingrese el numero a:"))
b = int(input("ingrese el numero b:"))
suma = 0 
p=0
if a > b:
	print("a debe ser mayor que b")
else: 
	for x in range(a,b+1):
		suma+= x**2 + 2*6
	print (suma)
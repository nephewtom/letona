Así es como lo he resuelto pero desconozco si hay una forma más sencilla.

Planteamiento:
El número de ovejas del pastor tiene que ser: 7xN = M
Donde N y M no pueden ser múltiplos de 2,3,4,5 ni 6.
Y además M debe cumplir las expresiones:
M = 2xA+1
M = 2xB+1
M = 2xC+1
M = 2xD+1
M = 2xE+1
donde A,B,C,D y E son enteros.

Resolución:
Para resolverlo se calculan los numeros primos entre 7 y 1000/7.
Se multiplica cada uno por 7.
Se comprueba si cada uno de ellos cumple las expresiones citadas

Se puede escribir un programita en Python que realice los cálculos del a siguiente manera:
def primeNumbers(lower, upper):
    p = []
    for num in range(lower, upper + 1):
        if num > 1: # prime numbers greater than 1
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                p.append(num)
    return p

def checkValidSheeps(m):
    x = m - 1
    if x%2 == 0:
       if x%3 == 0:
          if x%4 == 0:
             if x%5 == 0:
                if x%6 == 0:
                   return True
    return False

p = primeNumbers(7, 1000/7)
print p
mp = map(lambda x: x*7, p)
print mp
for x in mp:
    if checkValidSheeps(x):
        print 'Sheeps:', x

Resultado de la ejecución del programa:
$ python problema-ovejas-letona.py 
Numero valido de ovejas: 301
Numero valido de ovejas: 721

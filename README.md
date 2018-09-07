# El pastor y su rebaño

Un problema divertido de la Escuela de Pensamiento Matemático Miguel de Guzmán.
Publicado en el post: https://www.facebook.com/EPM.MigueldeGuzman/posts/1801185633283286
  
> Un problema serio:
>
> Un pastor solo sabía contar hasta 10, y sabía que tenía menos de mil ovejas. Cada noche las agrupaba. Si lo hacía de 2 en 2, o de 3 en 3, o de 4 en 4, o de 5 en 5, o de 6 en 6, siempre sobraba una, pero si lo hacía de 7 en 7, no sobraba ninguna. ¿Cuántas ovejas tenía el rebaño?
>
> JM LETONA.

Así es como lo he resuelto pero desconozco si hay una forma más sencilla.

## Planteamiento
El número de ovejas del pastor tiene que ser: `7xN = M`
Donde N y M no pueden ser múltiplos de 2,3,4,5 ni 6.
Y además M debe cumplir las expresiones:
```M = 2xA+1
M = 2xB+1
M = 2xC+1
M = 2xD+1
M = 2xE+1```
donde A,B,C,D y E son enteros.

## Resolución
Para resolverlo se calculan los numeros primos entre **7** y **1000/7**.
Se multiplica cada uno por 7.
Se comprueba si cada uno de ellos cumple las expresiones citadas

Se ha escrito el programita `letona.py` en Python que realica dichos.

## Ejecución
Resultado de la ejecución del programa:
```$ python problema-ovejas-letona.py 
Numero valido de ovejas: 301
Numero valido de ovejas: 721```

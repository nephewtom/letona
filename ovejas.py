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

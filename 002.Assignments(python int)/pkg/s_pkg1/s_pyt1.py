import math
def isPrime(n):
    if n <= 1:
        return 'no'
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return 'no'
    return 'yes'

def check(x):
    c=x//2
    print(c)
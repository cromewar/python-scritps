import time
import sys

sys.setrecursionlimit(10**6)

def factorial_no_recursivo(n):
    respueta = 1

    while n >= 1:
        respueta = respueta * n
        n = n - 1

    return respueta

def factorial_r(n):
    if n == 1:
        return n

    return factorial_r(n-1) * n     

if __name__ == '__main__':
    n = 10000

    comienzo = time.time()
    factorial_no_recursivo(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)

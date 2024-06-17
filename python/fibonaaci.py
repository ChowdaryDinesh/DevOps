# Fibonnaci series using dynamic programing

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]


def fib_for(n: int):
    a, b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a

print(fibonacci(10))
print(fib_for(10))
'''Function to return the first 1000 values of the fibonacci sequence using memoization'''

fibonacci_cache = {}

def fibonacci(n):
    # check input is a positive int
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # check for cached value, if found then return
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute n
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache value and return
    fibonacci_cache[n] = value
    return value


for n in range(1, 1001):
    print(n, ":", fibonacci(n))

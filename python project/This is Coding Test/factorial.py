#factorial

def factorial_(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_(5))

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

print(factorial(5))
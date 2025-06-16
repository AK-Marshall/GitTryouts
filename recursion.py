def recursionFactorial(n):
    if n == 0:
        return 1
    else:
        return n * recursionFactorial(n-1)

print(recursionFactorial(5))
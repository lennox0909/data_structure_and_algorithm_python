# 遞迴 Recursion
# n! n階

def factorial(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)


print(factorial(6))
import math
def middleDigit(n):
    digits = math.log10(n) + 1
    n = int((n // math.pow(10, digits // 2))) % 10
    return n
N = int(input("Enter the Digit to Find Center Value: "))
print(middleDigit(N))
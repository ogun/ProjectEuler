import fractions
import math

def isPrime(number):
    if number < 2:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        numbSqrt = int(math.sqrt(number))
        for i in range(5, numbSqrt + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False;
        return True

def isPalindromic(number):
    return str(number)[::-1] == str(number)

def fibonacciList(maxNumber):
    a, b = 1, 1
    while a < maxNumber:
        yield a
        a, b = b, a + b

def greatestCommonDivisor(*numbers):
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    if len(numbers) == 2:
        return fractions.gcd(numbers[0], numbers[1])

    firstNumber = numbers[0]
    returnValue = firstNumber
    for number in numbers[1:]:
        returnValue = fractions.gcd(returnValue, number)

    return returnValue

def lcm(a, b):
    return (a * b) // greatestCommonDivisor(a, b)

def leastCommonMultiple(*numbers):
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    firstNumber = numbers[0]
    returnValue = firstNumber
    for number in numbers[1:]:
        returnValue = lcm(returnValue, number)

    return returnValue
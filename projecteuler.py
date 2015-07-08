import math
import mathhelper


def problem1():
    """ Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    """
    return sum((x for x in range(1000) if x % 3 == 0 or x % 5 == 0))


def problem2():
    """ Even Fibonacci numbers
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    """
    tempFib = 1
    preFib = 1
    nextFib = tempFib + preFib
    returnValue = 0
    while nextFib < 4000000:
        if nextFib % 2 == 0:
            returnValue += nextFib
        tempFib = nextFib
        nextFib += preFib
        preFib = tempFib
    return returnValue


def problem3():
    """ Largest prime factor
    What is the largest prime factor of the number 600851475143 ?

    """
    constNumber = 600851475143
    for i in range(int(math.sqrt(constNumber)), 2, -1):
        if constNumber % i == 0 and mathhelper.isPrime(i):
            return i


def problem4():
    """ Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.

    """
    return max((x * y for x in range(100, 999) for y in range(100, 999) if mathhelper.isPalindromic(x * y)))
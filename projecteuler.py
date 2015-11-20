import math
import mathhelper
import itertools

def problem1():
    """ Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    """
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

def problem2():
    """ Even Fibonacci numbers
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    """
    returnValue = 0
    for number in mathhelper.fibonacciList(4000000):
        if number % 2 == 0:
            returnValue += number
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
    return max(x * y for (x, y) in itertools.product(range(100, 1000), range(100, 1000)) if mathhelper.isPalindromic(x * y))

def problem5():
    """ Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    """
    return mathhelper.leastCommonMultiple(*range(1, 21))

def problem6():
    """ Sum square difference
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    """
    return (sum(range(1, 101)) ** 2) - (sum(x ** 2 for x in range(1, 101)))

def problem7():
    """ 10001st prime
    What is the 10 001st prime number?

    """
    count = 0
    number = 1
    while True:
        number += 1

        if mathhelper.isPrime(number):
            count += 1

        if count == 10001:
            break
    return number

def problem8():
    """ Largest product in a series
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?

    """
    numberData = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    numberList = list(numberData)

    maxValue = 0
    for i in range(0, len(numberList))[:-12]:
        product = 1
        for number in numberList[i:i + 13]:
            product *= int(number)
        if product > maxValue:
            maxValue = product

    return maxValue
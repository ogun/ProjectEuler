"""Project Euler"""
import math
import itertools
import mathhelper


def problem1():
    """ Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

    """
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


def problem2():
    """ Even Fibonacci numbers
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.

    """
    return_value = 0
    for number in mathhelper.fibonacci_list(4000000):
        if number % 2 == 0:
            return_value += number
    return return_value


def problem3():
    """ Largest prime factor
    What is the largest prime factor of the number 600851475143 ?

    """
    const_number = 600851475143
    for i in range(int(math.sqrt(const_number)), 2, -1):
        if const_number % i == 0 and mathhelper.is_prime(i):
            return i


def problem4():
    """ Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two
    3-digit numbers.

    """
    return max(
        x * y for (x, y) in itertools.product(range(100, 1000), range(100, 1000)) if
        mathhelper.is_palindromic(x * y))


def problem5():
    """ Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
    remainder. What is the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20?

    """
    return mathhelper.least_common_multiple(*range(1, 21))


def problem6():
    """ Sum square difference
    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.

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

        if mathhelper.is_prime(number):
            count += 1

        if count == 10001:
            break
    return number


def problem8():
    """ Largest product in a series
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?

    """
    number_data = ("73167176531330624919225119674426574742355349194934"
                   "96983520312774506326239578318016984801869478851843"
                   "85861560789112949495459501737958331952853208805511"
                   "12540698747158523863050715693290963295227443043557"
                   "66896648950445244523161731856403098711121722383113"
                   "62229893423380308135336276614282806444486645238749"
                   "30358907296290491560440772390713810515859307960866"
                   "70172427121883998797908792274921901699720888093776"
                   "65727333001053367881220235421809751254540594752243"
                   "52584907711670556013604839586446706324415722155397"
                   "53697817977846174064955149290862569321978468622482"
                   "83972241375657056057490261407972968652414535100474"
                   "82166370484403199890008895243450658541227588666881"
                   "16427171479924442928230863465674813919123162824586"
                   "17866458359124566529476545682848912883142607690042"
                   "24219022671055626321111109370544217506941658960408"
                   "07198403850962455444362981230987879927244284909188"
                   "84580156166097919133875499200524063689912560717606"
                   "05886116467109405077541002256983155200055935729725"
                   "71636269561882670428252483600823257530420752963450")
    number_list = list(number_data)

    max_value = 0
    for i in range(0, len(number_list))[:-12]:
        product = 1
        for number in number_list[i:i + 13]:
            product *= int(number)
        if product > max_value:
            max_value = product

    return max_value


def problem9():
    """ Special Pythagorean triplet
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

    """
    for first in range(1, 1000 // 3):
        for second in range(first, 1000 // 2):
            third = 1000 - (first + second)
            if first ** 2 + second ** 2 == third ** 2:
                return first * second * third


def problem10():
    """ Summation of primes
    Find the sum of all the primes below two million.

    """
    return sum(x for x in range(2, 2000000) if mathhelper.is_prime(x))

print(problem1())
print(problem2())
print(problem3())
print(problem4())
print(problem5())
print(problem6())
print(problem7())
print(problem8())
print(problem9())
print(problem10())
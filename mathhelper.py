"""Matematik işlemleri için yardımcı modül"""
import math
import sys


def factor_count(number):
    """Verilen sayının toplam çarpan sayısını belirler"""
    if number == 0:
        return 0

    return_value = 1
    for prime_divisors in prime_divisor_list(number):
        return_value *= len(prime_divisors) + 1
    return return_value


def fibonacci_number_list(max_number):
    """Verilen sayıya kadar olan fibonacci sayılarını listeler
    max_number olarak None verilirse sys.maxsize'a kadar listeler"""
    current_number, next_number = 1, 1
    limit = sys.maxsize if max_number is None else int(max_number) + 1
    while current_number < limit:
        yield current_number
        current_number, next_number = next_number, current_number + next_number


def greatest_common_divisor(*numbers):
    """Verilen sayıların en büyük ortak bölenini belirler"""
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return abs(numbers[0])

    if len(numbers) == 2:
        return math.gcd(numbers[0], numbers[1])

    first_number = numbers[0]
    return_value = first_number
    for number in numbers[1:]:
        return_value = math.gcd(return_value, number)

    return return_value


def is_palindromic(number):
    """Verilen sayının palindromic olup olmadığını belirler"""
    number = abs(number)
    return str(number)[::-1] == str(number)


def is_prime(number):
    """Verilen sayının asal olup olmadığını belirler"""
    return_value = True

    if number < 2:
        return_value = False
    elif number < 4:
        return_value = True
    elif number % 2 == 0:
        return_value = False
    elif number < 9:
        return_value = True
    elif number % 3 == 0:
        return_value = False
    else:
        numb_sqrt = int(math.sqrt(number))
        for i in range(5, numb_sqrt + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False

    return return_value


def least_common_multiple(*numbers):
    """Verilen sayıların en küçük ortak katını belirler"""
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    if len(numbers) == 2:
        return int(numbers[0] * numbers[1]) // greatest_common_divisor(numbers[0], numbers[1])

    first_number = numbers[0]
    return_value = first_number
    for number in numbers[1:]:
        return_value = least_common_multiple(return_value, number)

    return return_value


def prime_divisor_list(number):
    """Verilen sayının asal çarpanlarını listeler
    Örn: 12 için [[2, 2], [3]]"""
    number = abs(number)

    if number == 0 or number == 1:
        return []

    if is_prime(number):
        return [[number]]

    return_value = []
    limit = int(number / 2) + 1
    for divisor in prime_number_list(limit):
        prime_divisor = []
        while number % divisor == 0:
            prime_divisor.append(divisor)
            number = number / divisor
        if len(prime_divisor) > 0:
            return_value.append(prime_divisor)

        if number == 1:
            return return_value


def prime_number_list(max_number):
    """Verilen sayıya kadar olan asal sayıları listeler
    max_number olarak None verilirse sys.maxsize'a kadar listeler"""
    limit = sys.maxsize if max_number is None else int(max_number) + 1
    for number in range(2, limit):
        if is_prime(number):
            yield number


def triangle_number_list(max_number):
    """Verilen sayıya kadar olan triangle sayıları listeler
    max_number olarak None verilirse sys.maxsize'a kadar listeler"""
    limit = sys.maxsize if max_number is None else int(max_number) + 1
    for number in range(1, limit):
        return_value = int(number * (number + 1) / 2)
        if return_value > limit:
            break
        yield return_value

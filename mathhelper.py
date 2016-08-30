"""Matematik işlemleri için yardımcı modül"""
import math


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


def is_palindromic(number):
    """Verilen sayının palindromic olup olmadığını belirler"""
    return str(number)[::-1] == str(number)


def fibonacci_list(max_number):
    """Verilen sayıya kadar olan fibonacci sayılarını listeler"""
    current_number, next_number = 1, 1
    while current_number < max_number:
        yield current_number
        current_number, next_number = next_number, current_number + next_number


def greatest_common_divisor(*numbers):
    """Verilen sayıların en büyük ortak bölenini belirler"""
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    if len(numbers) == 2:
        return math.gcd(numbers[0], numbers[1])

    first_number = numbers[0]
    return_value = first_number
    for number in numbers[1:]:
        return_value = math.gcd(return_value, number)

    return return_value


def least_common_multiple(*numbers):
    """Verilen sayıların en küçük ortak katını belirler"""
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    if len(numbers) == 2:
        return (numbers[0] * numbers[1]) // greatest_common_divisor(numbers[0], numbers[1])

    first_number = numbers[0]
    return_value = first_number
    for number in numbers[1:]:
        return_value = least_common_multiple(return_value, number)

    return return_value

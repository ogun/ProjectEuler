"""Matematik işlemleri için yardımcı modül"""
import math
import itertools


def collatz_sequence_chain_count(number):
    """Verilen sayının toplam collatz serisi sayısını belirler"""

    if number == 1:
        return 1

    chain_count = 1
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (3 * number) + 1
        chain_count += 1
    return chain_count


def create_number(number_list):
    """Verilen diziden oluşacak sayıyı belirler"""

    if len(number_list) == 0:
        return 0

    return_value = 0
    for index, step in enumerate(range(len(number_list), 0, -1)):
        return_value += int(number_list[index]) * (10 ** (step - 1))
    return return_value


def factor_count(number, proper=False):
    """Verilen sayının toplam çarpan sayısını belirler"""
    if number == 0:
        return 0

    return_value = 1
    for prime_divisors in prime_divisor_list(number):
        return_value *= len(prime_divisors) + 1

    if proper:
        return_value -= 1

    return return_value


def fibonacci_list(max_number):
    """Verilen sayıya kadar olan fibonacci sayılarını listeler
    max_number olarak None verilirse float('inf')'e kadar listeler"""
    current_number, next_number = 1, 1
    limit = float("inf") if max_number is None else int(max_number) + 1
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


def is_amicable(number):
    """Verilen sayının amicable olup olmadığını belirler"""
    factors = sum_factors(number, proper=True)

    return number != factors and number == sum_factors(factors, proper=True)


def is_palindromic(number):
    """Verilen sayının palindromic olup olmadığını belirler"""
    number = abs(number)
    return str(number)[::-1] == str(number)


def is_pandigital(number, start=1):
    """Verilen sayının pandigital olup olmadığını belirler"""

    number = abs(number)

    if number < start:
        return False

    digits = []
    if number == 0:
        digits.append(0)

    while number:
        digit = number % 10
        if digit < start or digit in digits:
            return False
        digits.append(digit)

        number //= 10

    if sorted(digits) == list(range(start, len(digits) + start)):
        return True

    return False


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
        return int(numbers[0] * numbers[1]) // greatest_common_divisor(
            numbers[0], numbers[1]
        )

    first_number = numbers[0]
    return_value = first_number
    for number in numbers[1:]:
        return_value = least_common_multiple(return_value, number)

    return return_value


def prime_divisor_list(number, with_group=True):
    """Verilen sayının asal çarpanlarını listeler
    Örn: 12 için [[2, 2], [3]]"""
    number = abs(number)

    if number in [0, 1]:
        return []

    if is_prime(number):
        if with_group:
            return [[number]]

        return [number]

    return_value = []
    limit = int(number / 2) + 1
    for divisor in prime_list(limit):
        if with_group:
            prime_divisor = []
        while number % divisor == 0:
            if with_group:
                prime_divisor.append(divisor)
            else:
                return_value.append(divisor)
            number = number / divisor
        if with_group and len(prime_divisor) > 0:
            return_value.append(prime_divisor)

        if number == 1:
            return return_value


def prime_list(max_number, reverse=False):
    """Verilen sayıya kadar olan asal sayıları listeler
    max_number olarak None verilirse float('inf')'e kadar listeler"""
    limit = float("inf") if max_number is None else int(max_number) + 1
    number = max_number if reverse else 6
    if reverse:
        if number > 6:
            if is_prime(number):
                yield number

            number -= number % 6

        while number > 5:
            bigger = number + 1
            if bigger < max_number and is_prime(bigger):
                yield bigger

            lower = number - 1
            if is_prime(lower):
                yield lower

            if number == 6:
                break
            number -= 6

        if number >= 3:
            yield 3

        if number >= 2:
            yield 2
    else:
        if limit > 2:
            yield 2
        if limit > 3:
            yield 3

        while number <= limit:
            lower = number - 1
            if is_prime(lower):
                yield lower

            bigger = number + 1
            if bigger < limit and is_prime(bigger):
                yield bigger
            number += 6


def product(number_list):
    """Verilen sayı listesinin çarpımını belirler"""
    return_value = 1
    for number in number_list:
        return_value *= number
    return return_value


def sum_digits(number):
    """Verilen sayının rakamlarının toplamını belirler"""
    number = abs(number)

    return_value = 0
    while number:
        return_value += number % 10
        number //= 10
    return return_value


def sum_factors(number, proper=False):
    """Verilan sayının çarpanlarının toplamını belirler"""

    if number == 0:
        return 0

    if number == 1 and proper:
        return 0

    prime_divisors = prime_divisor_list(number, with_group=False)

    sum_products = 1
    for element_count in range(1, len(prime_divisors) + 1):
        sum_products += sum(
            product(x)
            for x in set(itertools.combinations(prime_divisors, element_count))
        )

    if proper:
        sum_products -= abs(number)

    return sum_products


def sum_powers(number_list, power):
    """Verilen dizideki sayıların verilen üsse göre toplamını belirler"""

    if len(number_list) == 0:
        return 0

    return_value = 0
    for index in range(0, len(number_list)):
        return_value += int(number_list[index]) ** power
    return return_value


def sum_powers_of_digits(number, power):
    """Verilen sayıya ait rakamların verilen üsse göre toplamını belirler"""
    return_value = 0
    while number:
        return_value += (number % 10) ** power
        number //= 10
    return return_value


def triangle_list(max_number):
    """Verilen sayıya kadar olan triangle sayıları listeler
    max_number olarak None verilirse float('inf')'e kadar listeler"""
    limit = float("inf") if max_number is None else int(max_number) + 1
    number = 1
    while number <= limit:
        return_value = int(number * (number + 1) / 2)
        if return_value >= limit:
            break
        yield return_value
        number += 1

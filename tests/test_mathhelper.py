import unittest
import mathhelper


class TestMathHelper(unittest.TestCase):
    def test_collatz_sequence_chain_count(self):
        self.assertEqual(mathhelper.collatz_sequence_chain_count(1), 1)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(2), 2)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(3), 8)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(13), 10)

    def test_create_number(self):
        self.assertEqual(mathhelper.create_number(list("123")), 123)
        self.assertEqual(mathhelper.create_number(list("0123")), 123)
        self.assertEqual(mathhelper.create_number(list("9876")), 9876)
        self.assertEqual(mathhelper.create_number([4, 5, 6, 7, 8, 9]), 456789)

    def test_factor_count(self):
        self.assertEqual(mathhelper.factor_count(-5), 2)
        self.assertEqual(mathhelper.factor_count(-4), 3)
        self.assertEqual(mathhelper.factor_count(-3), 2)
        self.assertEqual(mathhelper.factor_count(-2), 2)
        self.assertEqual(mathhelper.factor_count(-1), 1)
        self.assertEqual(mathhelper.factor_count(0), 0)
        self.assertEqual(mathhelper.factor_count(1), 1)
        self.assertEqual(mathhelper.factor_count(2), 2)
        self.assertEqual(mathhelper.factor_count(4), 3)
        self.assertEqual(mathhelper.factor_count(5), 2)
        self.assertEqual(mathhelper.factor_count(6), 4)
        self.assertEqual(mathhelper.factor_count(21), 4)
        self.assertEqual(mathhelper.factor_count(28), 6)
        self.assertEqual(mathhelper.factor_count(-5, True), 1)
        self.assertEqual(mathhelper.factor_count(-4, True), 2)
        self.assertEqual(mathhelper.factor_count(-3, True), 1)
        self.assertEqual(mathhelper.factor_count(-2, True), 1)
        self.assertEqual(mathhelper.factor_count(-1, True), 0)
        self.assertEqual(mathhelper.factor_count(0, True), 0)
        self.assertEqual(mathhelper.factor_count(1, True), 0)
        self.assertEqual(mathhelper.factor_count(2, True), 1)
        self.assertEqual(mathhelper.factor_count(4, True), 2)
        self.assertEqual(mathhelper.factor_count(5, True), 1)
        self.assertEqual(mathhelper.factor_count(6, True), 3)
        self.assertEqual(mathhelper.factor_count(21, True), 3)
        self.assertEqual(mathhelper.factor_count(28, True), 5)

    def test_fibonacci_list(self):
        self.assertEqual(list(mathhelper.fibonacci_list(-5)), [])
        self.assertEqual(list(mathhelper.fibonacci_list(-1)), [])
        self.assertEqual(list(mathhelper.fibonacci_list(0)), [])
        self.assertEqual(list(mathhelper.fibonacci_list(1)), [1, 1])
        self.assertEqual(list(mathhelper.fibonacci_list(2)), [1, 1, 2])
        self.assertEqual(list(mathhelper.fibonacci_list(3)), [1, 1, 2, 3])
        self.assertEqual(list(mathhelper.fibonacci_list(10)), [1, 1, 2, 3, 5, 8])
        self.assertEqual(
            list(mathhelper.fibonacci_list(144)),
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],
        )

    def test_greatest_common_divisor(self):
        self.assertEqual(mathhelper.greatest_common_divisor(-1), 1)
        self.assertEqual(mathhelper.greatest_common_divisor(0), 0)
        self.assertEqual(mathhelper.greatest_common_divisor(-5, 10), 5)
        self.assertEqual(mathhelper.greatest_common_divisor(-5, 0), 5)
        self.assertEqual(mathhelper.greatest_common_divisor(5, 0), 5)
        self.assertEqual(mathhelper.greatest_common_divisor(-5, -1), 1)
        self.assertEqual(mathhelper.greatest_common_divisor(-5, 1), 1)
        self.assertEqual(mathhelper.greatest_common_divisor(8, 4), 4)
        self.assertEqual(mathhelper.greatest_common_divisor(13, 7), 1)
        self.assertEqual(mathhelper.greatest_common_divisor(-5, 10, 0), 5)
        self.assertEqual(mathhelper.greatest_common_divisor(1, 2, 4, 8, 16), 1)
        self.assertEqual(mathhelper.greatest_common_divisor(2, 4, 8, 16, 32), 2)

    def test_is_amicable_number(self):
        self.assertEqual(mathhelper.is_amicable(-1), False)
        self.assertEqual(mathhelper.is_amicable(0), False)
        self.assertEqual(mathhelper.is_amicable(1), False)
        self.assertEqual(mathhelper.is_amicable(11), False)
        self.assertEqual(mathhelper.is_amicable(13), False)
        self.assertEqual(mathhelper.is_amicable(220), True)
        self.assertEqual(mathhelper.is_amicable(284), True)
        self.assertEqual(mathhelper.is_amicable(1100), False)
        self.assertEqual(mathhelper.is_amicable(1184), True)

    def test_is_palindromic(self):
        self.assertEqual(mathhelper.is_palindromic(-1), True)
        self.assertEqual(mathhelper.is_palindromic(0), True)
        self.assertEqual(mathhelper.is_palindromic(1), True)
        self.assertEqual(mathhelper.is_palindromic(11), True)
        self.assertEqual(mathhelper.is_palindromic(13), False)
        self.assertEqual(mathhelper.is_palindromic(131), True)
        self.assertEqual(mathhelper.is_palindromic(199991), True)
        self.assertEqual(mathhelper.is_palindromic(1999991), True)
        self.assertEqual(mathhelper.is_palindromic(234667556), False)

    def test_is_pandigital(self):
        self.assertEqual(mathhelper.is_pandigital(-1), True)
        self.assertEqual(mathhelper.is_pandigital(0), False)
        self.assertEqual(mathhelper.is_pandigital(1), True)
        self.assertEqual(mathhelper.is_pandigital(10), False)
        self.assertEqual(mathhelper.is_pandigital(11), False)
        self.assertEqual(mathhelper.is_pandigital(12), True)
        self.assertEqual(mathhelper.is_pandigital(13), False)
        self.assertEqual(mathhelper.is_pandigital(21), True)
        self.assertEqual(mathhelper.is_pandigital(201), False)
        self.assertEqual(mathhelper.is_pandigital(131), False)
        self.assertEqual(mathhelper.is_pandigital(132), True)
        self.assertEqual(mathhelper.is_pandigital(1302), False)
        self.assertEqual(mathhelper.is_pandigital(199991), False)
        self.assertEqual(mathhelper.is_pandigital(1999991), False)
        self.assertEqual(mathhelper.is_pandigital(234667556), False)
        self.assertEqual(mathhelper.is_pandigital(234167589), True)
        self.assertEqual(mathhelper.is_pandigital(-1, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(0, start=0), True)
        self.assertEqual(mathhelper.is_pandigital(1, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(10, start=0), True)
        self.assertEqual(mathhelper.is_pandigital(11, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(12, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(13, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(21, start=0), False)
        self.assertEqual(mathhelper.is_pandigital(201, start=0), True)
        self.assertEqual(mathhelper.is_pandigital(131, start=0), False)

    def test_is_prime(self):
        self.assertEqual(mathhelper.is_prime(-5), False)
        self.assertEqual(mathhelper.is_prime(-4), False)
        self.assertEqual(mathhelper.is_prime(-3), False)
        self.assertEqual(mathhelper.is_prime(-2), False)
        self.assertEqual(mathhelper.is_prime(-1), False)
        self.assertEqual(mathhelper.is_prime(0), False)
        self.assertEqual(mathhelper.is_prime(1), False)
        self.assertEqual(mathhelper.is_prime(2), True)
        self.assertEqual(mathhelper.is_prime(3), True)
        self.assertEqual(mathhelper.is_prime(4), False)
        self.assertEqual(mathhelper.is_prime(5), True)
        self.assertEqual(mathhelper.is_prime(6), False)
        self.assertEqual(mathhelper.is_prime(7), True)

    def test_least_common_multiple(self):
        self.assertEqual(mathhelper.least_common_multiple(-1), -1)
        self.assertEqual(mathhelper.least_common_multiple(0), 0)
        self.assertEqual(mathhelper.least_common_multiple(-5, 10), -10)
        self.assertEqual(mathhelper.least_common_multiple(-5, 0), 0)
        self.assertEqual(mathhelper.least_common_multiple(5, 0), 0)
        self.assertEqual(mathhelper.least_common_multiple(-5, -1), 5)
        self.assertEqual(mathhelper.least_common_multiple(-5, 1), -5)
        self.assertEqual(mathhelper.least_common_multiple(8, 4), 8)
        self.assertEqual(mathhelper.least_common_multiple(13, 7), 91)
        self.assertEqual(mathhelper.least_common_multiple(-5, 10, 0), 0)
        self.assertEqual(mathhelper.least_common_multiple(1, 2, 4, 8, 16), 16)
        self.assertEqual(mathhelper.least_common_multiple(2, 4, 8, 16, 32), 32)

    def test_prime_divisor_list(self):
        self.assertEqual(list(mathhelper.prime_divisor_list(-5)), [[5]])
        self.assertEqual(list(mathhelper.prime_divisor_list(-4)), [[2, 2]])
        self.assertEqual(list(mathhelper.prime_divisor_list(-1)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(0)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(1)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(2)), [[2]])
        self.assertEqual(list(mathhelper.prime_divisor_list(3)), [[3]])
        self.assertEqual(list(mathhelper.prime_divisor_list(4)), [[2, 2]])
        self.assertEqual(list(mathhelper.prime_divisor_list(5)), [[5]])
        self.assertEqual(list(mathhelper.prime_divisor_list(6)), [[2], [3]])
        self.assertEqual(list(mathhelper.prime_divisor_list(12)), [[2, 2], [3]])
        self.assertEqual(list(mathhelper.prime_divisor_list(30)), [[2], [3], [5]])
        self.assertEqual(list(mathhelper.prime_divisor_list(-5, False)), [5])
        self.assertEqual(list(mathhelper.prime_divisor_list(-4, False)), [2, 2])
        self.assertEqual(list(mathhelper.prime_divisor_list(-1, False)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(0, False)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(1, False)), [])
        self.assertEqual(list(mathhelper.prime_divisor_list(2, False)), [2])
        self.assertEqual(list(mathhelper.prime_divisor_list(3, False)), [3])
        self.assertEqual(list(mathhelper.prime_divisor_list(4, False)), [2, 2])
        self.assertEqual(list(mathhelper.prime_divisor_list(5, False)), [5])
        self.assertEqual(list(mathhelper.prime_divisor_list(6, False)), [2, 3])
        self.assertEqual(list(mathhelper.prime_divisor_list(12, False)), [2, 2, 3])
        self.assertEqual(list(mathhelper.prime_divisor_list(30, False)), [2, 3, 5])

    def test_prime_list(self):
        self.assertEqual(list(mathhelper.prime_list(-5)), [])
        self.assertEqual(list(mathhelper.prime_list(-1)), [])
        self.assertEqual(list(mathhelper.prime_list(0)), [])
        self.assertEqual(list(mathhelper.prime_list(1)), [])
        self.assertEqual(list(mathhelper.prime_list(2)), [2])
        self.assertEqual(list(mathhelper.prime_list(3)), [2, 3])
        self.assertEqual(list(mathhelper.prime_list(10)), [2, 3, 5, 7])
        self.assertEqual(list(mathhelper.prime_list(17)), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(list(mathhelper.prime_list(18)), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(list(mathhelper.prime_list(19)), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(list(mathhelper.prime_list(20)), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(list(mathhelper.prime_list(21)), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(list(mathhelper.prime_list(22)), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(
            list(mathhelper.prime_list(23)), [2, 3, 5, 7, 11, 13, 17, 19, 23]
        )
        self.assertEqual(
            list(mathhelper.prime_list(24)), [2, 3, 5, 7, 11, 13, 17, 19, 23]
        )
        self.assertEqual(list(mathhelper.prime_list(-5, True)), [])
        self.assertEqual(list(mathhelper.prime_list(-1, True)), [])
        self.assertEqual(list(mathhelper.prime_list(0, True)), [])
        self.assertEqual(list(mathhelper.prime_list(1, True)), [])
        self.assertEqual(list(mathhelper.prime_list(2, True)), [2])
        self.assertEqual(list(mathhelper.prime_list(3, True)), [3, 2])
        self.assertEqual(list(mathhelper.prime_list(10, True)), [7, 5, 3, 2])
        self.assertEqual(
            list(mathhelper.prime_list(17, True)), [17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(18, True)), [17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(19, True)), [19, 17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(20, True)), [19, 17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(21, True)), [19, 17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(22, True)), [19, 17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(23, True)), [23, 19, 17, 13, 11, 7, 5, 3, 2]
        )
        self.assertEqual(
            list(mathhelper.prime_list(24, True)), [23, 19, 17, 13, 11, 7, 5, 3, 2]
        )

    def test_sum_digits(self):
        self.assertEqual(mathhelper.sum_digits(-1), 1)
        self.assertEqual(mathhelper.sum_digits(0), 0)
        self.assertEqual(mathhelper.sum_digits(1), 1)
        self.assertEqual(mathhelper.sum_digits(2), 2)
        self.assertEqual(mathhelper.sum_digits(21), 3)
        self.assertEqual(mathhelper.sum_digits(867), 21)
        self.assertEqual(mathhelper.sum_digits(99000009), 27)

    def test_sum_factors(self):
        self.assertEqual(mathhelper.sum_factors(-1), 1)
        self.assertEqual(mathhelper.sum_factors(0), 0)
        self.assertEqual(mathhelper.sum_factors(1), 1)
        self.assertEqual(mathhelper.sum_factors(2), 3)
        self.assertEqual(mathhelper.sum_factors(3), 4)
        self.assertEqual(mathhelper.sum_factors(4), 7)
        self.assertEqual(mathhelper.sum_factors(5), 6)
        self.assertEqual(mathhelper.sum_factors(6), 12)
        self.assertEqual(mathhelper.sum_factors(10), 18)
        self.assertEqual(mathhelper.sum_factors(12), 28)
        self.assertEqual(mathhelper.sum_factors(25), 31)
        self.assertEqual(mathhelper.sum_factors(-1, True), 0)
        self.assertEqual(mathhelper.sum_factors(0, True), 0)
        self.assertEqual(mathhelper.sum_factors(1, True), 0)
        self.assertEqual(mathhelper.sum_factors(2, True), 1)
        self.assertEqual(mathhelper.sum_factors(3, True), 1)
        self.assertEqual(mathhelper.sum_factors(4, True), 3)
        self.assertEqual(mathhelper.sum_factors(5, True), 1)
        self.assertEqual(mathhelper.sum_factors(6, True), 6)
        self.assertEqual(mathhelper.sum_factors(10, True), 8)
        self.assertEqual(mathhelper.sum_factors(12, True), 16)
        self.assertEqual(mathhelper.sum_factors(25, True), 6)

    def test_sum_powers(self):
        self.assertEqual(mathhelper.sum_powers([1, 2, 3], 3), 36)
        self.assertEqual(mathhelper.sum_powers([], 3), 0)
        self.assertEqual(mathhelper.sum_powers([1], 27), 1)
        self.assertEqual(mathhelper.sum_powers(list("345"), 2), 50)
        self.assertEqual(mathhelper.sum_powers([1, 2, 3, 4, 5], 0), 5)
        self.assertEqual(mathhelper.sum_powers([1, 2, 3, 4, 5], 1), 15)

    def test_sum_powers_of_digits(self):
        self.assertEqual(mathhelper.sum_powers_of_digits(123, 3), 36)
        self.assertEqual(mathhelper.sum_powers_of_digits(0, 3), 0)
        self.assertEqual(mathhelper.sum_powers_of_digits(1, 27), 1)
        self.assertEqual(mathhelper.sum_powers_of_digits(345, 2), 50)
        self.assertEqual(mathhelper.sum_powers_of_digits(12345, 0), 5)
        self.assertEqual(mathhelper.sum_powers_of_digits(12345, 1), 15)

    def test_triangle_list(self):
        self.assertEqual(list(mathhelper.triangle_list(-5)), [])
        self.assertEqual(list(mathhelper.triangle_list(-3)), [])
        self.assertEqual(list(mathhelper.triangle_list(-1)), [])
        self.assertEqual(list(mathhelper.triangle_list(-0)), [])
        self.assertEqual(list(mathhelper.triangle_list(1)), [1])
        self.assertEqual(list(mathhelper.triangle_list(2)), [1])
        self.assertEqual(list(mathhelper.triangle_list(3)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_list(4)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_list(5)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_list(6)), [1, 3, 6])
        self.assertEqual(list(mathhelper.triangle_list(27)), [1, 3, 6, 10, 15, 21])
        self.assertEqual(list(mathhelper.triangle_list(28)), [1, 3, 6, 10, 15, 21, 28])
        self.assertEqual(list(mathhelper.triangle_list(29)), [1, 3, 6, 10, 15, 21, 28])
        self.assertEqual(
            list(mathhelper.triangle_list(39)), [1, 3, 6, 10, 15, 21, 28, 36]
        )


if __name__ == "__main__":
    unittest.main()

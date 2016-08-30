import unittest
import mathhelper


class TestMathHelper(unittest.TestCase):
    def test_collatz_sequence_chain_count(self):
        self.assertEqual(mathhelper.collatz_sequence_chain_count(1), 1)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(2), 2)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(3), 8)
        self.assertEqual(mathhelper.collatz_sequence_chain_count(13), 10)

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

    def test_fibonacci_number_list(self):
        self.assertEqual(list(mathhelper.fibonacci_number_list(-5)), [])
        self.assertEqual(list(mathhelper.fibonacci_number_list(-1)), [])
        self.assertEqual(list(mathhelper.fibonacci_number_list(0)), [])
        self.assertEqual(list(mathhelper.fibonacci_number_list(1)), [1, 1])
        self.assertEqual(list(mathhelper.fibonacci_number_list(2)), [1, 1, 2])
        self.assertEqual(list(mathhelper.fibonacci_number_list(3)), [1, 1, 2, 3])
        self.assertEqual(list(mathhelper.fibonacci_number_list(10)), [1, 1, 2, 3, 5, 8])
        self.assertEqual(list(mathhelper.fibonacci_number_list(144)),
                         [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

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

    def test_prime_number_list(self):
        self.assertEqual(list(mathhelper.prime_number_list(-5)), [])
        self.assertEqual(list(mathhelper.prime_number_list(-1)), [])
        self.assertEqual(list(mathhelper.prime_number_list(0)), [])
        self.assertEqual(list(mathhelper.prime_number_list(1)), [])
        self.assertEqual(list(mathhelper.prime_number_list(2)), [2])
        self.assertEqual(list(mathhelper.prime_number_list(3)), [2, 3])
        self.assertEqual(list(mathhelper.prime_number_list(10)), [2, 3, 5, 7])
        self.assertEqual(list(mathhelper.prime_number_list(17)), [2, 3, 5, 7, 11, 13, 17])

    def test_sum_digits(self):
        self.assertEqual(mathhelper.sum_digits(-1), 1)
        self.assertEqual(mathhelper.sum_digits(0), 0)
        self.assertEqual(mathhelper.sum_digits(1), 1)
        self.assertEqual(mathhelper.sum_digits(2), 2)
        self.assertEqual(mathhelper.sum_digits(21), 3)
        self.assertEqual(mathhelper.sum_digits(867), 21)
        self.assertEqual(mathhelper.sum_digits(99000009), 27)

    def test_triangle_number_list(self):
        self.assertEqual(list(mathhelper.triangle_number_list(-5)), [])
        self.assertEqual(list(mathhelper.triangle_number_list(-3)), [])
        self.assertEqual(list(mathhelper.triangle_number_list(-1)), [])
        self.assertEqual(list(mathhelper.triangle_number_list(-0)), [])
        self.assertEqual(list(mathhelper.triangle_number_list(1)), [1])
        self.assertEqual(list(mathhelper.triangle_number_list(2)), [1])
        self.assertEqual(list(mathhelper.triangle_number_list(3)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_number_list(4)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_number_list(5)), [1, 3])
        self.assertEqual(list(mathhelper.triangle_number_list(6)), [1, 3, 6])
        self.assertEqual(list(mathhelper.triangle_number_list(27)), [1, 3, 6, 10, 15, 21])
        self.assertEqual(list(mathhelper.triangle_number_list(28)), [1, 3, 6, 10, 15, 21, 28])
        self.assertEqual(list(mathhelper.triangle_number_list(29)), [1, 3, 6, 10, 15, 21, 28])
        self.assertEqual(list(mathhelper.triangle_number_list(39)), [1, 3, 6, 10, 15, 21, 28, 36])

if __name__ == '__main__':
    unittest.main()

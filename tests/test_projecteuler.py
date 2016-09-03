import unittest
import projecteuler


class TestProjectEuler(unittest.TestCase):
    def test_problem1(self):
        self.assertEqual(projecteuler.problem1(), 233168)

    def test_problem2(self):
        self.assertEqual(projecteuler.problem2(), 4613732)

    def test_problem3(self):
        self.assertEqual(projecteuler.problem3(), 6857)

    def test_problem4(self):
        self.assertEqual(projecteuler.problem4(), 906609)

    def test_problem5(self):
        self.assertEqual(projecteuler.problem5(), 232792560)

    def test_problem6(self):
        self.assertEqual(projecteuler.problem6(), 25164150)

    def test_problem7(self):
        self.assertEqual(projecteuler.problem7(), 104743)

    def test_problem8(self):
        self.assertEqual(projecteuler.problem8(), 23514624000)

    def test_problem9(self):
        self.assertEqual(projecteuler.problem9(), 31875000)

    def test_problem10(self):
        self.assertEqual(projecteuler.problem10(), 142913828922)

    def test_problem11(self):
        self.assertEqual(projecteuler.problem11(), 70600674)

    def test_problem12(self):
        self.assertEqual(projecteuler.problem12(), 76576500)

    def test_problem13(self):
        self.assertEqual(projecteuler.problem13(), 5537376230)

    def test_problem14(self):
        self.assertEqual(projecteuler.problem14(), 837799)

    def test_problem15(self):
        self.assertEqual(projecteuler.problem15(), 137846528820)

    def test_problem16(self):
        self.assertEqual(projecteuler.problem16(), 1366)

    def test_problem18(self):
        self.assertEqual(projecteuler.problem18(), 1074)

    def test_problem19(self):
        self.assertEqual(projecteuler.problem19(), 171)

    def test_problem20(self):
        self.assertEqual(projecteuler.problem20(), 648)

    def test_problem21(self):
        self.assertEqual(projecteuler.problem21(), 31626)

    def test_problem22(self):
        self.assertEqual(projecteuler.problem22(), 871198282)

    def test_problem67(self):
        self.assertEqual(projecteuler.problem67(), 7273)

if __name__ == '__main__':
    unittest.main()

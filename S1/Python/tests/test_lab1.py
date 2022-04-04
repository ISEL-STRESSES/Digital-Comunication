import unittest
from S1.Python.Lab1.fibonacci import fibonacci
from S1.Python.Lab1.fibonacci import fib
from S1.Python.Lab1.prog_arithmetic import prog_arithmetic
from S1.Python.Lab1.prog_arithmetic import prog_arithmetic_by_term
from S1.Python.Lab1.most_frequent_elem import most_frequent_elem


class TestFibonacci(unittest.TestCase):
    def test_fib_elements(self):  # test fibonacci sequence values
        self.assertEqual(fib(0), 0)  # fib0 = 0
        self.assertEqual(fib(1), 1)  # fib1 = 1
        self.assertEqual(fib(2), 1)  # fib2 = 2
        self.assertEqual(fib(3), 2)  # fib3 = 2
        self.assertEqual(fib(4), 3)  # fib4 = 3
        self.assertEqual(fib(5), 5)  # fib5 = 5
        self.assertEqual(fib(7), 13)  # fib7 = 13
        self.assertEqual(fib(10), 55)  # fib10 = 55

    def test_array_of_fib(self):    # test if values are correctly allocated to return array
        result = fibonacci(10)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], fib(1))
        self.assertEqual(result[2], fib(3))
        self.assertEqual(result[5], fib(6))
        self.assertEqual(result[9], fib(10))

    def test_fail_conditions(self):     # test behaviour for invalid parameters
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(-1), [])
        self.assertEqual(fibonacci(-5), [])


class TestProgArithmetic(unittest.TestCase):
    def test_prog_arithmetic_first(self):     # test arithmetic progression by term for first term
        self.assertEqual(prog_arithmetic_by_term(2, 2, 1), 2)  # progr_arithm u1 = 2
        self.assertEqual(prog_arithmetic_by_term(3, 5, 1), 3)  # progr_arithm u1 = 3
        self.assertEqual(prog_arithmetic_by_term(5, 1, 1), 5)  # progr_arithm u1 = 5

    def test_prog_arithmetic_by_term(self):     # test arithmetic progression by term
        self.assertEqual(prog_arithmetic_by_term(2, 2, 2), 4)  # progr_arithm u2 = 2 + 2*1
        self.assertEqual(prog_arithmetic_by_term(3, 5, 3), 13)  # progr_arithm u3 = 3 + 5*2
        self.assertEqual(prog_arithmetic_by_term(5, 1, 5), 9)  # progr_arithm u5 = 5 + 1*4

    def test_array_prog_arithmetic(self):     # test if values are correctly allocated to return array
        result = prog_arithmetic(10, 3, 5)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], prog_arithmetic_by_term(3, 5, 1))
        self.assertEqual(result[1], prog_arithmetic_by_term(3, 5, 2))
        self.assertEqual(result[3], prog_arithmetic_by_term(3, 5, 4))
        self.assertEqual(result[5], prog_arithmetic_by_term(3, 5, 6))
        self.assertEqual(result[7], prog_arithmetic_by_term(3, 5, 8))
        self.assertEqual(result[9], prog_arithmetic_by_term(3, 5, 10))

    def test_fail_conditions(self):     # test behaviour for invalid parameters
        self.assertEqual(prog_arithmetic(0, 5, 2), [])
        self.assertEqual(prog_arithmetic(-3, 1, 8), [])

#class TestMostFrequentElem(unittest.TestCase):
#    def test_most_frequent_elem(self):     # test most frequent element
#        res = most_frequent_elem("test_most_freq.txt")
#        self.assertIsNotNone(res)
#        self.assertEqual(res, [('a', 3)])


if __name__ == '__main__':
    unittest.main()

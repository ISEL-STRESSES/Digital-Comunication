import unittest
from S1.Python.Lab1.fibonacci import fibonacci
from S1.Python.Lab1.fibonacci import fib


class TestFibonacci(unittest.TestCase):
    def test_fib_elements(self):  # test fibanacci sequence values
        result = fibonacci(10)
        self.assertEqual(fib(0), 0)  # fib0
        self.assertEqual(fib(1), 1)  # fib1
        self.assertEqual(fib(2), 1)  # fib2
        self.assertEqual(fib(3), 2)  # fib3
        self.assertEqual(fib(4), 3)  # fib4
        self.assertEqual(fib(5), 5)  # fib5
        self.assertEqual(fib(7), 13)  # fib7
        self.assertEqual(fib(10), 55)  # fib10


    def test_array_of_fib(self):
        result = fibonacci(10)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], fib(1))
        self.assertEqual(result[2], fib(3))
        self.assertEqual(result[5], fib(6))
        self.assertEqual(result[9], fib(10))

    def test_fail_conditions(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(-1), [])
        self.assertEqual(fibonacci(-5), [])


if __name__ == '__main__':
    unittest.main()

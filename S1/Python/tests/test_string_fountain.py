import unittest
from S1.Python.StringFountain.string_fountain import string_fountain


class MyTestCase(unittest.TestCase):
    def test_string_fountain(self):
        res = string_fountain(["a", "b", "c", "d"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3, False, False)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 3)
        res = string_fountain(["a", "bb", "b", "d"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 1, False, False)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 1)

    def test_elements_with_element_with_full_prob(self):
        res = string_fountain(["a", "b", "c", "d"], [0, 0, 0, 1], 3, False, False)
        self.assertEqual(res, ["d", "d", "d"])

    def test_fail_conditions(self):     # test behaviour for invalid parameters
        self.assertEqual(string_fountain(["a", "a", "a"], [1 / 5, 1 / 5, 3 / 5], 3, False, False), None)      # repeated elements
        self.assertEqual(string_fountain(["a", "b", "c"], [1 / 5, 1 / 5, 1 / 5], 3, False, False), None)      # sum fmp < 1
        self.assertEqual(string_fountain(["a", "b", "c"], [1 / 5, 1 / 5, 4 / 5], 3, False, False), None)      # sum fmp > 1
        self.assertEqual(string_fountain(["a", "b", "c"], [1 / 5, 1 / 5], 3, False, False), None)     # size strs != size fmp


if __name__ == '__main__':
    unittest.main()

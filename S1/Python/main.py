from S1.Python.Lab1.fibonacci import fibonacci
from S1.Python.Lab1.prog_arithmetic import prog_arithmetic
from S1.Python.Lab1.most_frequent_elem import most_frequent_elem
from string_fountain import string_fountain

if __name__ == '__main__':
    print(fibonacci(10))
    print(prog_arithmetic(10, 2, 1))
    print(most_frequent_elem("test.txt"))
    print(most_frequent_elem("tests/test_most_freq.txt"))
    print(string_fountain(["a", "b", "c", "d"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3))
    print(string_fountain(["a", "bb", "b", "d"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 2))

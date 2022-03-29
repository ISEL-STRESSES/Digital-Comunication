from fibonacci import fibonacci
from most_frequent_numb import most_frequent_numb
from prog_arithmetic import prog_arithmetic
from string_fountain import string_fountain

if __name__ == '__main__':
    print(fibonacci(10))
    print(prog_arithmetic(10, 2, 1))
    print(most_frequent_numb("test.txt"))
    print(string_fountain(["a", "b", "c", "d"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3))

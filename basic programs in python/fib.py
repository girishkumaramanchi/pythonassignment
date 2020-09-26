import unittest
# """
def print_n_fib_series(val):
    a = 0
    b = 1
    for i in range(1, val + 1):
        if i == 1:
            print(a, end=" ")
        elif i == 2:
            print(b, end=" ")
        else:
            c = a + b
            a = b
            b = c
            print(c, end=" ")
# """

def fib_n(val):
    a = 0
    b = 1
    for i in range(1, val + 1):
        if i == 1:
            n = a
            # print(a, end=" ")
        elif i == 2:
            n = b
            # print(b, end=" ")
        else:
            c = a + b
            a = b
            b = c
            n = c
            # print(c, end=" ")
    return n


val = int(input("Enter your value: "))
fib_n(val)
print_n_fib_series(val)


class Fib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib_n(1), 0)
        self.assertEqual(fib_n(2), 1)
        self.assertEqual(fib_n(10), 34)
        self.assertEqual(fib_n(13), 144)



if __name__ == '__main__':
    unittest.main()

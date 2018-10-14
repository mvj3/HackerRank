from nose.tools import assert_equal

"""
The key point to write the correct Fibonacci program is to understand
how to change [first, second].
"""


class Math(object):

    def fib_iterative(self, nth):
        first = 0
        second = 1
        while nth >= 1:
            first, second = second, first + second
            nth -= 1
        return first

    def fib_recursive(self, nth):
        if nth <= 1:
            return nth
        else:
            return self.fib_recursive(nth-1) + self.fib_recursive(nth-2)

    def fib_recursive_tail_optmization(self, nth):
        def f(first, second, nth):
            if nth <= 0:
                return first
            else:
                return f(second, first + second, nth - 1)
        return f(0, 1, nth)


class TestFib(object):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        assert_equal(result, expected)
        print('Success: test_fib')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_recursive_tail_optmization)
    import sys
    sys.setrecursionlimit(100000)
    print(math.fib_recursive_tail_optmization(9000))
    # math.fib_recursive(500)
    test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    main()

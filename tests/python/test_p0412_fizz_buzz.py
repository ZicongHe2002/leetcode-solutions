import unittest

from python.p0412_fizz_buzz import Solution


PERIOD = (None, None, 'Fizz', None, 'Buzz', 'Fizz', None, None, 'Fizz', 'Buzz', None, 'Fizz', None, None, 'FizzBuzz')


def period_oracle(size):
    answer = []
    for start in range(0, size, 15):
        for offset, label in enumerate(PERIOD, 1):
            value = start + offset
            if value > size:
                break
            answer.append(label if label is not None else str(value))
    return answer


class FizzBuzzPeriodTests(unittest.TestCase):
    def test_every_small_prefix_against_explicit_period_table(self):
        for size in range(1, 1001):
            result = Solution().fizzBuzz(size)
            self.assertIs(type(result), list)
            self.assertTrue(all(type(value) is str for value in result))
            self.assertEqual(result, period_oracle(size))

    def test_rule_intersections_order_and_maximum_length(self):
        self.assertEqual(Solution().fizzBuzz(1), ['1'])
        self.assertEqual(Solution().fizzBuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(Solution().fizzBuzz(15)[-1], 'FizzBuzz')
        result = Solution().fizzBuzz(10000)
        self.assertEqual(result, period_oracle(10000))
        self.assertEqual(len(result), 10000)
        self.assertEqual(result.count('FizzBuzz'), 666)
        self.assertEqual(result.count('Fizz'), 2667)
        self.assertEqual(result.count('Buzz'), 1334)


if __name__ == '__main__':
    unittest.main()

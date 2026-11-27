from itertools import product
import unittest

from python.p0284_peeking_iterator import PeekingIterator


class ListIterator:
    def __init__(self, values):
        self.values = values[:]
        self.position = 0
        self.next_calls = 0

    def hasNext(self):
        return self.position < len(self.values)

    def next(self):
        if not self.hasNext():
            raise AssertionError('read beyond underlying iterator')
        value = self.values[self.position]
        self.position += 1
        self.next_calls += 1
        return value


class PeekingIteratorContractTests(unittest.TestCase):
    def check_program(self, values, program):
        underlying = ListIterator(values)
        wrapper = PeekingIterator(underlying)
        position = 0
        for operation in program:
            if operation == 'h':
                self.assertIs(type(wrapper.hasNext()), bool)
                self.assertEqual(wrapper.hasNext(), position < len(values))
            elif position == len(values):
                break
            elif operation == 'p':
                consumed = underlying.next_calls
                self.assertEqual(wrapper.peek(), values[position])
                self.assertEqual(wrapper.peek(), values[position])
                self.assertEqual(underlying.next_calls, consumed)
            else:
                self.assertEqual(wrapper.next(), values[position])
                position += 1
        while position < len(values):
            self.assertTrue(wrapper.hasNext())
            self.assertEqual(wrapper.next(), values[position])
            position += 1
        self.assertFalse(wrapper.hasNext())
        self.assertEqual(underlying.next_calls, len(values))
        self.assertEqual(underlying.values, values)

    def test_all_small_data_and_legal_operation_prefixes(self):
        cases = 0
        for size in range(4):
            for values in product((-1, 0, 1), repeat=size):
                for length in range(6):
                    for program in product('pnh', repeat=length):
                        self.check_program(list(values), program)
                        cases += 1
        self.assertEqual(cases, 14560)

    def test_long_sequences_zero_negative_and_empty_underlying(self):
        self.check_program(list(range(1000)), 'hppn' * 1000)
        self.check_program([0, -1, 0, 1], 'pphppnhnppn')
        self.check_program([], 'hhh')


if __name__ == '__main__':
    unittest.main()

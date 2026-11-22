import unittest
from itertools import product

from python.p0901_online_stock_span import StockSpanner


class OnlineSpanTests(unittest.TestCase):
    def test_all_small_price_sequences_against_raw_history_scans(self):
        sequences = calls = 0
        for size in range(9):
            for prices in product((1, 2, 3), repeat=size):
                sequences += 1
                tracker, history = StockSpanner(), []
                for price in prices:
                    expected, index = 1, len(history) - 1
                    while index >= 0 and history[index] <= price:
                        expected += 1
                        index -= 1
                    result = tracker.next(price)
                    self.assertIs(type(result), int)
                    self.assertEqual(result, expected)
                    history.append(price)
                    calls += 1
        self.assertEqual((sequences, calls), (9841, 73812))

    def test_maximum_call_count_equal_prices_and_instance_isolation(self):
        tracker = StockSpanner()
        for price in range(1, 10001):
            self.assertEqual(tracker.next(price), price)
        tracker = StockSpanner()
        for price in range(10000, 0, -1):
            self.assertEqual(tracker.next(price), 1)
        tracker = StockSpanner()
        for day in range(1, 10001):
            self.assertEqual(tracker.next(100000), day)
        first, second = StockSpanner(), StockSpanner()
        self.assertEqual(first.next(100), 1)
        self.assertEqual(second.next(50), 1)
        self.assertEqual(first.next(80), 1)
        self.assertEqual(second.next(60), 2)
        self.assertEqual(first.next(100), 3)


if __name__ == '__main__':
    unittest.main()

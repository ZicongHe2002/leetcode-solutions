import unittest
from itertools import combinations
from unittest.mock import patch

import python.p0710_random_pick_with_blacklist as implementation


class BlacklistPickTests(unittest.TestCase):
    def test_every_small_blacklist_maps_each_rank_once_to_allowed_set(self):
        subsets = 0
        for n in range(1, 9):
            for size in range(n):
                for selected in combinations(range(n), size):
                    subsets += 1
                    for order in {selected, selected[::-1]}:
                        blacklist = list(order)
                        before = blacklist[:]
                        remaining = n - len(blacklist)
                        obj = implementation.Solution(n, blacklist)
                        with patch.object(implementation, 'randrange', side_effect=range(remaining)) as source:
                            results = [obj.pick() for _ in range(remaining)]
                            self.assertEqual(source.call_count, remaining)
                            self.assertTrue(all(call.args == (remaining,) for call in source.call_args_list))
                        self.assertTrue(all(type(value) is int for value in results))
                        self.assertEqual(set(results), set(range(n)) - set(blacklist))
                        self.assertEqual(len(set(results)), remaining)
                        self.assertEqual(blacklist, before)
        self.assertEqual(subsets, 502)

    def test_billion_range_hundred_thousand_blacklist_and_twenty_thousand_picks(self):
        n = 10**9
        limit = n - 100000
        blacklist = list(range(50000)) + list(range(limit, limit + 50000))
        before = blacklist[:]
        obj = implementation.Solution(n, blacklist)
        blocked = set(blacklist)
        for rank in (0, 49999, 50000, limit // 2, limit - 1):
            with patch.object(implementation, 'randrange', return_value=rank) as source:
                value = obj.pick()
                source.assert_called_once_with(limit)
            self.assertTrue(0 <= value < n and value not in blocked)
        self.assertEqual(blacklist, before)
        single = implementation.Solution(100000, list(range(99999)))
        with patch.object(implementation, 'randrange', return_value=0) as source:
            self.assertEqual(single.pick(), 99999)
            source.assert_called_once_with(1)
        empty = implementation.Solution(n, [])
        with patch.object(implementation, 'randrange', return_value=123456789) as source:
            for _ in range(20000):
                self.assertEqual(empty.pick(), 123456789)
            self.assertEqual(source.call_count, 20000)
            self.assertTrue(all(call.args == (n,) for call in source.call_args_list))


if __name__ == '__main__':
    unittest.main()

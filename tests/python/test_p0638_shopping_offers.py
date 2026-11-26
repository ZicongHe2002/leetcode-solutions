import random
import unittest
from itertools import combinations_with_replacement, product

from python.p0638_shopping_offers import Solution


def enumerate_bundle_counts(price, special, needs):
    def choose(index, remaining):
        if index == len(special):
            return sum(quantity * unit for quantity, unit in zip(remaining, price))
        offer = special[index]
        maximum = min(quantity // used for quantity, used in zip(remaining, offer[:-1]) if used)
        return min(times * offer[-1] + choose(index + 1,
                   [quantity - times * used for quantity, used in zip(remaining, offer[:-1])])
                   for times in range(maximum + 1))
    return choose(0, needs)


class ShoppingOfferTests(unittest.TestCase):
    def check(self, price, special, needs, expected=None):
        before = (price[:], [offer[:] for offer in special], needs[:])
        if expected is None:
            expected = enumerate_bundle_counts(price, special, needs)
        actual = Solution().shoppingOffers(price, special, needs)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual((price, special, needs), before)

    def test_exhaustive_small_offers_and_seeded_samples_against_usage_counts(self):
        one_dimensional = [(quantity, cost) for quantity in range(1, 4) for cost in range(6)]
        checks = 0
        for price, need in product(range(4), range(5)):
            for offers in combinations_with_replacement(one_dimensional, 2):
                self.check([price], [list(offer) for offer in offers], [need])
                checks += 1
        self.assertEqual(checks, 3420)
        kinds = [quantities + (cost,) for quantities in ((1, 0), (0, 1), (1, 1), (2, 1))
                 for cost in range(5)]
        for price in product((0, 2), repeat=2):
            for needs in product(range(3), repeat=2):
                for offers in combinations_with_replacement(kinds, 2):
                    self.check(list(price), [list(offer) for offer in offers], list(needs))
                    checks += 1
        self.assertEqual(checks, 10980)
        rng = random.Random(638)
        for _ in range(100):
            count = rng.randint(1, 4)
            price = [rng.randrange(6) for _ in range(count)]
            needs = [rng.randrange(4) for _ in range(count)]
            offers = []
            for _ in range(rng.randint(1, 4)):
                quantities = [rng.randrange(4) for _ in range(count)]
                if not any(quantities):
                    quantities[0] = 1
                offers.append(quantities + [rng.randrange(11)])
            self.check(price, offers, needs)

    def test_maximum_dimensions_offers_free_goods_and_no_overbuying(self):
        self.check([10] * 6, [[1] * 6 + [1] for _ in range(100)], [10] * 6, 10)
        self.check([10] * 6, [[50] * 6 + [0] for _ in range(100)], [10] * 6, 600)
        self.check([0] * 6, [[1] * 6 + [0] for _ in range(100)], [10] * 6, 0)
        self.check([2, 3], [[1, 1, 0]], [10, 10], 0)
        self.check([10], [[2, 0]], [1], 10)
        self.check([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2], 14)
        self.check([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1], 11)


if __name__ == '__main__':
    unittest.main()

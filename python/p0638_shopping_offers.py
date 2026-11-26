from functools import lru_cache


class Solution:
    def shoppingOffers(self, price, special, needs):
        offers = [tuple(offer) for offer in special
                  if all(quantity <= need for quantity, need in zip(offer[:-1], needs))
                  and offer[-1] < sum(quantity * unit for quantity, unit in zip(offer[:-1], price))]

        @lru_cache(None)
        def minimum(remaining):
            best = sum(quantity * unit for quantity, unit in zip(remaining, price))
            for offer in offers:
                if offer[-1] >= best:
                    continue
                after = tuple(quantity - used for quantity, used in zip(remaining, offer[:-1]))
                if all(quantity >= 0 for quantity in after):
                    best = min(best, offer[-1] + minimum(after))
            return best

        return minimum(tuple(needs))

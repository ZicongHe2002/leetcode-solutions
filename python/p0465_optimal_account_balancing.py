class Solution:
    def minTransfers(self, transactions):
        ledger = {}
        for sender, receiver, amount in transactions:
            ledger[sender] = ledger.get(sender, 0) - amount
            ledger[receiver] = ledger.get(receiver, 0) + amount
        balances = [value for value in ledger.values() if value]
        size = len(balances)
        totals = [0] * (1 << size)
        groups = [0] * (1 << size)
        for mask in range(1, 1 << size):
            bit = mask & -mask
            totals[mask] = totals[mask ^ bit] + balances[bit.bit_length() - 1]
            remaining = mask
            best = 0
            while remaining:
                bit = remaining & -remaining
                best = max(best, groups[mask ^ bit])
                remaining ^= bit
            groups[mask] = best + (totals[mask] == 0)
        return size - groups[-1]

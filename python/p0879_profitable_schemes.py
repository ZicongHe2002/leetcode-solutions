class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        modulus = 10**9 + 7
        ways = [[0] * (minProfit + 1) for _ in range(n + 1)]
        ways[0][0] = 1
        for people,gain in zip(group,profit):
            for used in range(n,people - 1,-1):
                for earned in range(minProfit + 1):
                    following = min(minProfit,earned + gain)
                    ways[used][following] = (ways[used][following] + ways[used - people][earned]) % modulus
        return sum(row[minProfit] for row in ways) % modulus

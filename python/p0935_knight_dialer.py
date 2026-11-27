class Solution:
    def knightDialer(self, n):
        neighbors = ((4,6),(6,8),(7,9),(4,8),(0,3,9),(),(0,1,7),(2,6),(1,3),(2,4))
        modulus = 10**9 + 7
        ways = [1] * 10
        for _ in range(1,n):
            ways = [sum(ways[previous] for previous in neighbors[digit]) % modulus for digit in range(10)]
        return sum(ways) % modulus

class Solution:
    def numPermsDISequence(self, s):
        modulus = 10**9 + 7
        ways = [1]
        for relation in s:
            following = [0] * (len(ways) + 1)
            total = 0
            if relation == 'I':
                for rank in range(len(following)):
                    following[rank] = total
                    if rank < len(ways):
                        total = (total + ways[rank]) % modulus
            else:
                for rank in range(len(ways) - 1,-1,-1):
                    total = (total + ways[rank]) % modulus
                    following[rank] = total
            ways = following
        return sum(ways) % modulus

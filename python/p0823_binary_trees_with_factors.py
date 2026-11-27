class Solution:
    def numFactoredBinaryTrees(self, arr):
        values = sorted(arr)
        ways = {}
        modulus = 10**9 + 7
        for index,root in enumerate(values):
            count = 1
            for left_index in range(index):
                left = values[left_index]
                if root % left == 0:
                    right = root // left
                    if right in ways:
                        count = (count + ways[left] * ways[right]) % modulus
            ways[root] = count
        return sum(ways.values()) % modulus

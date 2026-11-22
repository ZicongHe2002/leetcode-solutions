class Solution:
    def numTrees(self, n):
        counts = [0] * (n + 1)
        counts[0] = 1
        for nodes in range(1, n + 1):
            for left_size in range(nodes):
                counts[nodes] += counts[left_size] * counts[nodes - 1 - left_size]
        return counts[n]

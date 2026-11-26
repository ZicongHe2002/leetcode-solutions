from collections import deque


class Solution:
    def minMutation(self, startGene, endGene, bank):
        if startGene == endGene:
            return 0
        remaining = set(bank)
        if endGene not in remaining:
            return -1
        remaining.discard(startGene)
        queue = deque([(startGene, 0)])
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for index, original in enumerate(gene):
                for letter in 'ACGT':
                    if letter == original:
                        continue
                    following = gene[:index] + letter + gene[index + 1:]
                    if following in remaining:
                        remaining.remove(following)
                        queue.append((following, steps + 1))
        return -1

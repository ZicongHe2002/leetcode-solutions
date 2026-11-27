class Solution:
    def numSimilarGroups(self, strs):
        parent = list(range(len(strs)))
        sizes = [1] * len(strs)
        groups = len(strs)

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def similar(first, second):
            mismatch = []
            for left,right in zip(first,second):
                if left != right:
                    mismatch.append((left,right))
                    if len(mismatch) > 2:
                        return False
            return (not mismatch or len(mismatch) == 2
                    and mismatch[0][0] == mismatch[1][1]
                    and mismatch[0][1] == mismatch[1][0])

        for first in range(len(strs)):
            for second in range(first):
                left,right = find(first),find(second)
                if left != right and similar(strs[first],strs[second]):
                    if sizes[left] < sizes[right]:
                        left,right = right,left
                    parent[right] = left
                    sizes[left] += sizes[right]
                    groups -= 1
        return groups

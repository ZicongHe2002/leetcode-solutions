class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for first,second in zip(s1,s2):
            left,right = find(ord(first) - ord('a')),find(ord(second) - ord('a'))
            if left != right:
                parent[max(left,right)] = min(left,right)
        return ''.join(chr(ord('a') + find(ord(char) - ord('a'))) for char in baseStr)

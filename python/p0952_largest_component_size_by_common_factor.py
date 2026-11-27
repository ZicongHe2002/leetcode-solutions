from collections import Counter


class Solution:
    def largestComponentSize(self, nums):
        parent = list(range(len(nums)))
        sizes = [1] * len(nums)
        owner = {}

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def attach(index, factor):
            if factor not in owner:
                owner[factor] = index
                return
            first,second = find(index),find(owner[factor])
            if first != second:
                if sizes[first] < sizes[second]:
                    first,second = second,first
                parent[second] = first
                sizes[first] += sizes[second]

        for index,original in enumerate(nums):
            value = original
            factor = 2
            while factor * factor <= value:
                if value % factor == 0:
                    attach(index,factor)
                    while value % factor == 0:
                        value //= factor
                factor = 3 if factor == 2 else factor + 2
            if value > 1:
                attach(index,value)
        return max(Counter(find(index) for index in range(len(nums))).values())

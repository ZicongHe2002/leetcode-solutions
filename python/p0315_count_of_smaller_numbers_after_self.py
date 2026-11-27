class Solution:
    def countSmaller(self, nums):
        ranks = {value: index + 1 for index, value in enumerate(sorted(set(nums)))}
        tree = [0] * (len(ranks) + 1)
        answer = [0] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            position = ranks[nums[index]]
            query = position - 1
            smaller = 0
            while query:
                smaller += tree[query]
                query -= query & -query
            answer[index] = smaller
            while position < len(tree):
                tree[position] += 1
                position += position & -position
        return answer

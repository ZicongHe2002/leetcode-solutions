from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, count in counts.items():
            buckets[count].append(value)
        answer = []
        for count in range(len(nums), 0, -1):
            for value in buckets[count]:
                answer.append(value)
                if len(answer) == k:
                    return answer

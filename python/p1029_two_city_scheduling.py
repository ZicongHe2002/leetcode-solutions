class Solution:
    def twoCitySchedCost(self, costs):
        ordered = sorted(costs,key=lambda pair:pair[0] - pair[1])
        half = len(ordered) // 2
        return sum(pair[0] if index < half else pair[1] for index,pair in enumerate(ordered))

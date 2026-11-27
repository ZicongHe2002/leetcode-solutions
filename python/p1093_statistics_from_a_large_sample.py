class Solution:
    def sampleStats(self, count):
        total = sum(count)
        minimum = next(value for value, frequency in enumerate(count) if frequency)
        maximum = next(value for value in range(len(count) - 1, -1, -1) if count[value])
        mean = sum(value * frequency for value, frequency in enumerate(count)) / total
        mode = max(range(len(count)), key=count.__getitem__)
        left_rank, right_rank = (total - 1) // 2, total // 2
        cumulative = 0
        middle_sum = 0
        for value, frequency in enumerate(count):
            following = cumulative + frequency
            if cumulative <= left_rank < following:
                middle_sum += value
            if cumulative <= right_rank < following:
                middle_sum += value
            cumulative = following
        return [float(minimum), float(maximum), mean, middle_sum / 2, float(mode)]

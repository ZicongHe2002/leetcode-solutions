class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        pending = []
        for day, temperature in enumerate(temperatures):
            while pending and temperature > temperatures[pending[-1]]:
                previous = pending.pop()
                answer[previous] = day - previous
            pending.append(day)
        return answer

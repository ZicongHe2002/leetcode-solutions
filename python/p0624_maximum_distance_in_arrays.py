class Solution:
    def maxDistance(self, arrays):
        smallest, largest = arrays[0][0], arrays[0][-1]
        answer = 0
        for index in range(1, len(arrays)):
            current = arrays[index]
            answer = max(answer, abs(current[-1] - smallest), abs(largest - current[0]))
            smallest = min(smallest, current[0])
            largest = max(largest, current[-1])
        return answer

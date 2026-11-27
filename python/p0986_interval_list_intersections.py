class Solution:
    def intervalIntersection(self, firstList, secondList):
        first = second = 0
        result = []
        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0],secondList[second][0])
            end = min(firstList[first][1],secondList[second][1])
            if start <= end:
                result.append([start,end])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return result

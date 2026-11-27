class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        first = second = third = 0
        answer = []
        while first < len(arr1) and second < len(arr2) and third < len(arr3):
            a, b, c = arr1[first], arr2[second], arr3[third]
            if a == b == c:
                answer.append(a)
                first += 1
                second += 1
                third += 1
            else:
                minimum = min(a, b, c)
                first += a == minimum
                second += b == minimum
                third += c == minimum
        return answer

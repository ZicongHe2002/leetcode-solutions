class Solution:
    def constructArray(self, n, k):
        answer = []
        low, high = 1, k + 1
        while low <= high:
            answer.append(low)
            low += 1
            if low <= high:
                answer.append(high)
                high -= 1
        answer.extend(range(k + 2, n + 1))
        return answer

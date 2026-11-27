class Solution:
    def numFriendRequests(self, ages):
        frequency = [0] * 121
        for age in ages:
            frequency[age] += 1
        prefix = [0] * 121
        for age in range(1,121):
            prefix[age] = prefix[age - 1] + frequency[age]
        answer = 0
        for age in range(15,121):
            eligible = prefix[age] - prefix[age // 2 + 7]
            answer += frequency[age] * (eligible - 1)
        return answer

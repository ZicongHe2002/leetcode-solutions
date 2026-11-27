class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        rows, columns = len(str1), len(str2)
        lcs = [[0] * (columns + 1) for _ in range(rows + 1)]
        for first in range(1, rows + 1):
            for second in range(1, columns + 1):
                if str1[first - 1] == str2[second - 1]:
                    lcs[first][second] = lcs[first - 1][second - 1] + 1
                else:
                    lcs[first][second] = max(lcs[first - 1][second], lcs[first][second - 1])
        first, second = rows, columns
        answer = []
        while first and second:
            if str1[first - 1] == str2[second - 1]:
                answer.append(str1[first - 1])
                first -= 1
                second -= 1
            elif lcs[first - 1][second] >= lcs[first][second - 1]:
                answer.append(str1[first - 1])
                first -= 1
            else:
                answer.append(str2[second - 1])
                second -= 1
        while first:
            first -= 1
            answer.append(str1[first])
        while second:
            second -= 1
            answer.append(str2[second])
        return ''.join(reversed(answer))

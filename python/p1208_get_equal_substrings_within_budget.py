class Solution:
    def equalSubstring(self, s, t, maxCost):
        left = spent = answer = 0
        for right in range(len(s)):
            spent += abs(ord(s[right]) - ord(t[right]))
            while spent > maxCost:
                spent -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            answer = max(answer, right - left + 1)
        return answer

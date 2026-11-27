class Solution:
    def diStringMatch(self, s):
        low,high = 0,len(s)
        result = []
        for relation in s:
            if relation == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result

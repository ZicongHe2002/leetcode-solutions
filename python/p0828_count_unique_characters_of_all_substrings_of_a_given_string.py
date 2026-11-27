class Solution:
    def uniqueLetterString(self, s):
        previous = {}
        answer = 0
        for index,char in enumerate(s):
            before,last = previous.get(char,(-1,-1))
            answer += (last - before) * (index - last)
            previous[char] = last,index
        for before,last in previous.values():
            answer += (last - before) * (len(s) - last)
        return answer

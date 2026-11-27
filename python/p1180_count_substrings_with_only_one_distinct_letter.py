class Solution:
    def countLetters(self, s):
        answer = run = 0
        previous = None
        for letter in s:
            run = run + 1 if letter == previous else 1
            answer += run
            previous = letter
        return answer

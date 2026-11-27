class Solution:
    def calculateTime(self, keyboard, word):
        positions = {letter: index for index, letter in enumerate(keyboard)}
        current = answer = 0
        for letter in word:
            following = positions[letter]
            answer += abs(following - current)
            current = following
        return answer

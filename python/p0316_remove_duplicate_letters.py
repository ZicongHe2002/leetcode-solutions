class Solution:
    def removeDuplicateLetters(self, s):
        last = {character: index for index, character in enumerate(s)}
        chosen, included = [], set()
        for index, character in enumerate(s):
            if character in included:
                continue
            while chosen and chosen[-1] > character and last[chosen[-1]] > index:
                included.remove(chosen.pop())
            chosen.append(character)
            included.add(character)
        return ''.join(chosen)

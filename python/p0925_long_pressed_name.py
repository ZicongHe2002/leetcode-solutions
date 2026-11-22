class Solution:
    def isLongPressedName(self, name, typed):
        matched = 0
        for index, character in enumerate(typed):
            if matched < len(name) and character == name[matched]:
                matched += 1
            elif index == 0 or character != typed[index - 1]:
                return False
        return matched == len(name)

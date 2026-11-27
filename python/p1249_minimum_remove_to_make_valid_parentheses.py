class Solution:
    def minRemoveToMakeValid(self, s):
        opened = []
        removed = set()
        for index, letter in enumerate(s):
            if letter == '(':
                opened.append(index)
            elif letter == ')':
                if opened:
                    opened.pop()
                else:
                    removed.add(index)
        removed.update(opened)
        return ''.join(letter for index, letter in enumerate(s) if index not in removed)

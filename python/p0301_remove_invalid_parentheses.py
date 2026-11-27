class Solution:
    def removeInvalidParentheses(self, s):
        def valid(text):
            balance = 0
            for character in text:
                if character == '(':
                    balance += 1
                elif character == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        level = {s}
        while level:
            answers = [text for text in level if valid(text)]
            if answers:
                return answers
            following = set()
            for text in level:
                for index, character in enumerate(text):
                    if character not in '()':
                        continue
                    if index and text[index - 1] == character:
                        continue
                    following.add(text[:index] + text[index + 1:])
            level = following
        return []

class Solution:
    def isValid(self, code):
        if not code:
            return False
        stack = []
        index = 0
        while index < len(code):
            if index > 0 and not stack:
                return False
            if code.startswith('<![CDATA[', index):
                if not stack:
                    return False
                end = code.find(']]>', index + 9)
                if end < 0:
                    return False
                index = end + 3
            elif code.startswith('</', index):
                end = code.find('>', index + 2)
                if end < 0:
                    return False
                name = code[index + 2:end]
                if not stack or stack[-1] != name:
                    return False
                stack.pop()
                index = end + 1
            elif code[index] == '<':
                end = code.find('>', index + 1)
                if end < 0:
                    return False
                name = code[index + 1:end]
                if not 1 <= len(name) <= 9 or not all('A' <= ch <= 'Z' for ch in name):
                    return False
                stack.append(name)
                index = end + 1
            else:
                if not stack:
                    return False
                index += 1
        return not stack

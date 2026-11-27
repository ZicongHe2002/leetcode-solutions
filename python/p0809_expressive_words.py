class Solution:
    def expressiveWords(self, s, words):
        def groups(text):
            result = []
            for char in text:
                if result and result[-1][0] == char:
                    result[-1][1] += 1
                else:
                    result.append([char,1])
            return result

        target = groups(s)

        def matches(word):
            candidate = groups(word)
            if len(candidate) != len(target):
                return False
            return all(char == other and count >= original
                       and (count == original or count >= 3)
                       for (char,count),(other,original) in zip(target,candidate))

        return sum(matches(word) for word in words)

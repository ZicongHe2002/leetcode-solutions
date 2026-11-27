class Solution:
    def camelMatch(self, queries, pattern):
        def matches(query):
            position = 0
            for char in query:
                if position < len(pattern) and char == pattern[position]:
                    position += 1
                elif char.isupper():
                    return False
            return position == len(pattern)

        return [matches(query) for query in queries]

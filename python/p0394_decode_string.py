class Solution:
    def decodeString(self, s):
        frames, parts = [], []
        repeat = 0
        for character in s:
            if '0' <= character <= '9':
                repeat = repeat * 10 + ord(character) - ord('0')
            elif character == '[':
                frames.append((parts, repeat))
                parts, repeat = [], 0
            elif character == ']':
                previous, times = frames.pop()
                previous.append(''.join(parts) * times)
                parts = previous
            else:
                parts.append(character)
        return ''.join(parts)

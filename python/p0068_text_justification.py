class Solution:
    def fullJustify(self, words, maxWidth):
        result, start = [], 0
        while start < len(words):
            end, letters = start, 0
            while end < len(words) and letters + len(words[end]) + end - start <= maxWidth:
                letters += len(words[end])
                end += 1
            slots = end - start - 1
            if end == len(words) or slots == 0:
                line = ' '.join(words[start:end])
                result.append(line + ' ' * (maxWidth - len(line)))
            else:
                base, extra = divmod(maxWidth - letters, slots)
                pieces = []
                for offset in range(end - start):
                    pieces.append(words[start + offset])
                    if offset < slots:
                        pieces.append(' ' * (base + (offset < extra)))
                result.append(''.join(pieces))
            start = end
        return result

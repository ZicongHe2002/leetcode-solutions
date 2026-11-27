class Solution:
    def movesToStamp(self, stamp, target):
        text = list(target)
        width = len(stamp)
        used = [False] * max(0,len(text) - width + 1)
        erased = 0
        moves = []
        while erased < len(text):
            progress = False
            for start in range(len(used)):
                if used[start]:
                    continue
                changes = False
                for offset in range(width):
                    char = text[start + offset]
                    if char != '?' and char != stamp[offset]:
                        break
                    if char != '?':
                        changes = True
                else:
                    used[start] = True
                    if not changes:
                        continue
                    for offset in range(width):
                        if text[start + offset] != '?':
                            text[start + offset] = '?'
                            erased += 1
                    moves.append(start)
                    progress = True
            if not progress:
                return []
        return moves[::-1]

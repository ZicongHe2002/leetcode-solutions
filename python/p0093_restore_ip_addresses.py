class Solution:
    def restoreIpAddresses(self, s):
        result, parts = [], []

        def search(position):
            if len(parts) == 4:
                if position == len(s):
                    result.append('.'.join(parts))
                return
            slots = 4 - len(parts)
            remaining = len(s) - position
            if not slots <= remaining <= 3 * slots:
                return
            for width in range(1, 4):
                piece = s[position:position + width]
                if len(piece) != width:
                    break
                if width > 1 and piece[0] == '0':
                    break
                if int(piece) > 255:
                    break
                parts.append(piece)
                search(position + width)
                parts.pop()

        search(0)
        return result

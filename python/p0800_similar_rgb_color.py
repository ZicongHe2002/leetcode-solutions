class Solution:
    def similarRGB(self, color):
        parts = []
        for offset in (1,3,5):
            value = int(color[offset:offset + 2],16)
            nearest = (value + 8) // 17
            parts.append(format(17 * nearest,'02x'))
        return '#' + ''.join(parts)

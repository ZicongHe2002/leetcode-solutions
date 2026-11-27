class Solution:
    def pathInZigZagTree(self, label):
        path = []
        while label:
            path.append(label)
            level = label.bit_length() - 1
            first = 1 << level
            last = (1 << (level + 1)) - 1
            label = (first + last - label) // 2
        return path[::-1]

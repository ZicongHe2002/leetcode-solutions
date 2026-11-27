class Solution:
    def isValidSerialization(self, preorder):
        if not preorder:
            return False
        slots = 1
        start = 0
        for end in range(len(preorder) + 1):
            if end == len(preorder) or preorder[end] == ',':
                if slots == 0:
                    return False
                slots += -1 if preorder[start] == '#' else 1
                start = end + 1
        return slots == 0

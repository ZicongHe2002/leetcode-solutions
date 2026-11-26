class Solution:
    def preorder(self, root):
        if root is None:
            return []
        result = [root.val]
        pending = [iter(root.children or ())]
        while pending:
            child = next(pending[-1], None)
            if child is None:
                pending.pop()
            else:
                result.append(child.val)
                pending.append(iter(child.children or ()))
        return result

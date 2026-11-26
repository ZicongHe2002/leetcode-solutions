def _preorder_tokens(root):
    pending = [root]
    while pending:
        node = pending.pop()
        if node is None:
            yield None
        else:
            yield node.val
            pending.append(node.right)
            pending.append(node.left)


class Solution:
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        pattern = list(_preorder_tokens(subRoot))
        prefix = [0] * len(pattern)
        matched = 0
        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            prefix[index] = matched
        matched = 0
        for token in _preorder_tokens(root):
            while matched and token != pattern[matched]:
                matched = prefix[matched - 1]
            if token == pattern[matched]:
                matched += 1
            if matched == len(pattern):
                return True
        return False

class Solution:
    def tree2str(self, root):
        if root is None:
            return ''
        pieces = []
        pending = [root]
        while pending:
            item = pending.pop()
            if isinstance(item, str):
                pieces.append(item)
                continue
            pieces.append(str(item.val))
            if item.right is not None:
                pending.extend((')', item.right, '('))
            if item.left is not None:
                pending.extend((')', item.left, '('))
            elif item.right is not None:
                pending.append('()')
        return ''.join(pieces)

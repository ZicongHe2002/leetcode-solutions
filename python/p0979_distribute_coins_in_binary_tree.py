class Solution:
    def distributeCoins(self, root):
        balance = {None:0}
        stack = [(root,False)]
        moves = 0
        while stack:
            node,ready = stack.pop()
            if node is None:
                continue
            if not ready:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))
            else:
                left,right = balance[node.left],balance[node.right]
                moves += abs(left) + abs(right)
                balance[node] = node.val + left + right - 1
        return moves

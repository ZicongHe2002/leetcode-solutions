class Solution:
    def numComponents(self, head, nums):
        included = set(nums)
        components = 0
        node = head
        while node is not None:
            if node.val in included and (node.next is None or node.next.val not in included):
                components += 1
            node = node.next
        return components

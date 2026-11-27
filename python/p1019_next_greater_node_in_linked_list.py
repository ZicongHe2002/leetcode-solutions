class Solution:
    def nextLargerNodes(self, head):
        answer = []
        waiting = []
        node = head
        while node is not None:
            while waiting and waiting[-1][1] < node.val:
                index,_ = waiting.pop()
                answer[index] = node.val
            waiting.append((len(answer),node.val))
            answer.append(0)
            node = node.next
        return answer

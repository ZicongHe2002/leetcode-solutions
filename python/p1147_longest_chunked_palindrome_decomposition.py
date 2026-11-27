class Solution:
    def longestDecomposition(self, text):
        left, right = 0, len(text) - 1
        left_chunk = right_chunk = ''
        answer = 0
        while left < right:
            left_chunk += text[left]
            right_chunk = text[right] + right_chunk
            if left_chunk == right_chunk:
                answer += 2
                left_chunk = right_chunk = ''
            left += 1
            right -= 1
        if left == right or left_chunk:
            answer += 1
        return answer

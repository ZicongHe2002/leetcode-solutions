class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def ordered(left_length, right_length):
            best_left = answer = 0
            for right_end in range(left_length + right_length,len(nums) + 1):
                split = right_end - right_length
                best_left = max(best_left,prefix[split] - prefix[split - left_length])
                answer = max(answer,best_left + prefix[right_end] - prefix[split])
            return answer

        return max(ordered(firstLen,secondLen),ordered(secondLen,firstLen))

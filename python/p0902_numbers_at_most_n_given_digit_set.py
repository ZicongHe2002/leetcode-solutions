class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        bound = str(n)
        choices = len(digits)
        allowed = set(digits)
        answer = sum(choices**length for length in range(1,len(bound)))
        for index,char in enumerate(bound):
            smaller = sum(digit < char for digit in digits)
            answer += smaller * choices**(len(bound) - index - 1)
            if char not in allowed:
                return answer
        return answer + 1

class Solution:
    def leastOpsExpressTarget(self, x, target):
        positive = negative = 0
        exponent = 0
        while target:
            target,digit = divmod(target,x)
            if exponent == 0:
                positive = 2 * digit
                negative = 2 * (x - digit)
            else:
                positive,negative = (
                    min(positive + digit * exponent,negative + (digit + 1) * exponent),
                    min(positive + (x - digit) * exponent,negative + (x - digit - 1) * exponent))
            exponent += 1
        return min(positive,negative + exponent) - 1

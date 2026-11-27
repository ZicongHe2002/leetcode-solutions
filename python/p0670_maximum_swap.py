class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))
        last = [-1] * 10
        for index, digit in enumerate(digits):
            last[int(digit)] = index
        for index, digit in enumerate(digits):
            for larger in range(9, int(digit), -1):
                if last[larger] > index:
                    other = last[larger]
                    digits[index], digits[other] = digits[other], digits[index]
                    return int(''.join(digits))
        return num

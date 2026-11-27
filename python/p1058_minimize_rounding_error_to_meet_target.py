class Solution:
    def minimizeError(self, prices, target):
        lower_sum = 0
        fractions = []
        for price in prices:
            integer,decimal = price.split('.')
            lower_sum += int(integer)
            fractional = int(decimal)
            if fractional:
                fractions.append(fractional)
        upward = target - lower_sum
        if upward < 0 or upward > len(fractions):
            return '-1'
        fractions.sort(reverse=True)
        error = sum(fractions)
        for fractional in fractions[:upward]:
            error += 1000 - 2 * fractional
        return f'{error // 1000}.{error % 1000:03d}'

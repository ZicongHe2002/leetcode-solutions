class Solution:
    def dayOfYear(self, date):
        year, month, day = map(int, date.split('-'))
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        lengths = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(lengths[:month - 1]) + day

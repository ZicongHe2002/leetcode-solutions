from datetime import date


class Solution:
    def dayOfTheWeek(self, day, month, year):
        names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        return names[date(year, month, day).weekday()]

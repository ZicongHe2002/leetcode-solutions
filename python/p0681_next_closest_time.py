class Solution:
    def nextClosestTime(self, time):
        allowed = set(time.replace(':', ''))
        start = int(time[:2]) * 60 + int(time[3:])
        for elapsed in range(1, 1441):
            hour, minute = divmod((start + elapsed) % 1440, 60)
            candidate = f'{hour:02d}:{minute:02d}'
            if all(char in allowed for char in candidate if char != ':'):
                return candidate

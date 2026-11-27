class Solution:
    def videoStitching(self, clips, time):
        ordered = sorted(clips)
        covered = index = used = 0
        while covered < time:
            following = covered
            while index < len(ordered) and ordered[index][0] <= covered:
                following = max(following,ordered[index][1])
                index += 1
            if following == covered:
                return -1
            covered = following
            used += 1
        return used

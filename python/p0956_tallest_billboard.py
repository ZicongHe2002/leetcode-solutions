class Solution:
    def tallestBillboard(self, rods):
        best = {0:0}
        for rod in rods:
            following = best.copy()
            for difference,shorter in best.items():
                high_difference = difference + rod
                following[high_difference] = max(following.get(high_difference,0),shorter)
                low_difference = abs(difference - rod)
                low_height = shorter + min(difference,rod)
                following[low_difference] = max(following.get(low_difference,0),low_height)
            best = following
        return best[0]

class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position,speed),reverse=True)
        fleets = 0
        last_numerator,last_denominator = -1,1
        for location,velocity in cars:
            numerator = target - location
            if numerator * last_denominator > last_numerator * velocity:
                fleets += 1
                last_numerator,last_denominator = numerator,velocity
        return fleets

import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            # Calculate total hours needed with speed = mid
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            # If Koko can finish within h hours
            if hours <= h:
                ans = mid
                right = mid - 1   # Try smaller speed
            else:
                left = mid + 1    # Increase speed

        return ans
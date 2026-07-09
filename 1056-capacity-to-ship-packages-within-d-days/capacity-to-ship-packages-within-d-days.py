class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            days_used = 1
            load = 0

            for weight in weights:
                if load + weight <= mid:
                    load += weight
                else:
                    days_used += 1
                    load = weight

            if days_used <= days:
                right = mid
            else:
                left = mid + 1

        return left
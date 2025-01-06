from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 0
        # Loop through possible counts of 2-steps
        for two_steps in range(n // 2 + 1):
            one_steps = n - 2 * two_steps
            # Calculate permutations using combinations formula
            total_ways += comb(one_steps + two_steps, two_steps)
        return total_ways

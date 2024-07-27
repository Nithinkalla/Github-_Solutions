class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = list(set(nums))
        y = sorted(x)
        if len(y) >= 3:
            return y[-3]
        else:
            return y[-1]
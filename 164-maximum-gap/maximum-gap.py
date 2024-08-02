class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        return max(diff)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        start = nums.index(target)
        end = len(nums) - 1 - nums[::-1].index(target)
        return [start,end]
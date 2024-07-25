class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while x < len(nums):
            if nums.count(nums[x]) >= 3:
                nums.pop(x)
            else:
                x += 1
        return len(nums)
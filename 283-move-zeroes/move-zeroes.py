class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        y = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[y] = nums[i]
                y += 1
        for i in range(y,len(nums)):
            nums[i] = 0
        
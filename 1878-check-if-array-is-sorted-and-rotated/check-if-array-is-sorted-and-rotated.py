class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                x += 1
        if nums[len(nums) - 1] > nums[0]:
            x += 1
        if x <= 1:
            return True
        return False
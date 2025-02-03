class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
        #return min(nums)
        # mini = nums[0]
        # for i in nums:
        #     if i < mini:
        #         mini = i
        # return mini

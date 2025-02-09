class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                return nums[i] + 1
        return nums[-1] + 1 if nums[0] == 0 else 0 
        # x = len(nums)
        # lst = list(range(x + 1))
        # for i in range(x + 1):
        #     if lst[i] not in nums:
        #         return lst[i]
        # miss = set(lst) - set(nums)
        # return miss.pop()
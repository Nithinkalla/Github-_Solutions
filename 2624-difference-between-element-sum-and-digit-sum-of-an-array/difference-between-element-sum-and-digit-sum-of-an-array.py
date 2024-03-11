class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        total = sum(nums)
        for i in nums:
            for j in str(i):
                sum1 += int(j)
        if total > sum1:
            return total - sum1
        else:
            return sum1 - total
        
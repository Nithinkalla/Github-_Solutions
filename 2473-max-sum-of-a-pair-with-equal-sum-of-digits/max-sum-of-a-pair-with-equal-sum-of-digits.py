class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        ans = -1
        for i in range(len(nums)):
            sumd = 0
            for j in str(nums[i]):
                sumd += int(j)
            if sumd not in d:
                d[sumd] = nums[i]
            else:
                ans = max(d[sumd] + nums[i],ans)
                d[sumd] = max(d[sumd],nums[i])
        return ans

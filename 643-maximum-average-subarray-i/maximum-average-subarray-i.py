class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        w_sum = sum(nums[:k])
        max_sum = w_sum
        for i in range(n - k):
            w_sum = w_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum,w_sum)
        return max_sum / k
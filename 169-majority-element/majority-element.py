class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)
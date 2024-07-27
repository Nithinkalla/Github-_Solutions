class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        y = sorted(nums)
        return y[-k]
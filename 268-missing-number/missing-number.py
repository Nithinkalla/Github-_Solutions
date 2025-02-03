class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        lst = list(range(x + 1))
        miss = set(lst) - set(nums)
        return miss.pop()
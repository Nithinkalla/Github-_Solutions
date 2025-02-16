class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x1 = set(range(1,len(nums) + 1))
        x2 = set(nums)
        return list(x1 - x2)
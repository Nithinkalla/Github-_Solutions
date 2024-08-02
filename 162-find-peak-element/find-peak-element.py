class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        x,y = 0,len(nums) - 1
        while x < y:
            mid = (x + y) // 2
            if nums[mid] > nums[mid + 1]:
                y = mid
            else:
                x = mid + 1
        return x
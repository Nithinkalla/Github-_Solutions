class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        x = 0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                nums[x],nums[i] = nums[i],nums[x]
                x += 1
        return len(s)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = []
        y = 0
        for i in range(len(nums)):
            if nums[i] != val:
                x.append(nums[i])
                nums[y],nums[i] = nums[i],nums[y]
                y += 1
        return len(x)
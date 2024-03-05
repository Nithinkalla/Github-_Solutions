class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        x,y = 0,0
        for i in nums:
            if i > 0:
                x+=1
            elif i < 0:
                y+=1
        if x>y:
            return x
        else:
            return y
        
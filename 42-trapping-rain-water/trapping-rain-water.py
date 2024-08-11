class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lm = height[left]
        rm = height[right]
        water = 0
        while left < right:
            if lm < rm:
                left += 1
                lm = max(lm,height[left])
                water += lm - height[left]
            else:
                right -= 1
                rm = max(rm,height[right])
                water += rm - height[right]
        return water
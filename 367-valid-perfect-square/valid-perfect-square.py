class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        low,high = 0,num
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
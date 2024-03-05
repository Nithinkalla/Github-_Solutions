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
# we can max function for returning the x or y
# in this case i used if-else because of runtime
# the runtime for max function is 113ms for if-else = 110 
        
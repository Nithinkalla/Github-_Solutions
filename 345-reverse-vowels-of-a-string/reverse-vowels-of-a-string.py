class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vow = {'a','e','i','o','u','A','E','I','O','U'}
        l,r = 0,len(lst) - 1
        while l < r:
            while(l < r and lst[l] not in vow):
                l += 1
            while(r > l and lst[r] not in vow):
                r -= 1
            lst[l] , lst[r] = lst[r],lst[l]
            l += 1
            r -= 1
        return "".join(lst)
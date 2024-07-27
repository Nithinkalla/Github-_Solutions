class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        jnstr = "".join(y)
        rev = jnstr[::-1]
        if jnstr == rev:
            return True
        else:
            return False
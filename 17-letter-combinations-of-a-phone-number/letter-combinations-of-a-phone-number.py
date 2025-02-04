from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d_to_l = {
            "2" : "abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        l_g = [d_to_l[i] for i in digits]
        return ["".join(i) for i in product(*l_g)]
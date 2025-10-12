class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        lst = []
        for i in s:
            if i in mapping.values():
                lst.append(i)
            elif i in mapping:
                if not lst or lst[-1] not in mapping[i]:
                    return False
                lst.pop()
        return not lst
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace("()","").replace("[]","").replace("{}","")
        # return not s
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s
        # x =[]
        # length_part = len(part)
        # length_end = part[-1]
        # for i in s:
        #     x.append(i)
        #     if i == length_end and len(x) >= length_part:
        #         if "".join(x[-length_part:]) == part:
        #             del x[-length_part:]
        # return "".join(x)
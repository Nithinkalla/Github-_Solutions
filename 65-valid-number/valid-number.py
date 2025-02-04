class Solution:
    def isNumber(self, s: str) -> bool:
        if s.strip().lower() in ["inf", "-inf","+inf", "infinity","+infinity", "-infinity", "nan"]:
            return False
        try:
            n = float(s)
            return True
        except ValueError:
            return False

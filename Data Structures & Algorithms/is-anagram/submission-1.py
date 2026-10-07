class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        if ss == tt:
            return True
        else:
            return False

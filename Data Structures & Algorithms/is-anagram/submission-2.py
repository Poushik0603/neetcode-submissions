class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for c in s:
            if c in hash1:
                hash1[c] = hash1[c] + 1
            else:
                hash1[c] = 1
        for c in t:
            if c in hash2:
                hash2[c] = hash2[c] + 1
            else:
                hash2[c] = 1
        if hash1 == hash2:
            return True
        else:
            return False
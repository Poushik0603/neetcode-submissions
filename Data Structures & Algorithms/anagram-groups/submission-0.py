class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashs = {}
        for word in strs:
            anag = list(word)
            anag.sort()
            key = ''.join(anag)
            if key in hashs:
                hashs[key].append(word)
            else:
                hashs[key] = [word]
        return list(hashs.values())
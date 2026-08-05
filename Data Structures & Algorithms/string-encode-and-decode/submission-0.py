class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + str(word)
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i+=1
            i+=1
            length = int(length)
            result.append(s[i:i+length])
            i += length
        return result


            

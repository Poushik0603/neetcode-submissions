class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()
        n = len(result)
        for i in range(0,n//2):
            if result[i] != result[n-i-1]:
                return False
        return True
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        check = ''
        brackets = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for ch in s:
            if ch in brackets.keys():
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                check = stack.pop()
                if brackets[check] != ch:
                    return False
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        guide = {')': '(', ']': '[', '}': '{'}
        result = []
        for i in range(0, len(s)):
            if len(result) == 0:
                if s[i] in guide.keys():
                    return False
                result.append(s[i])
            else:
                if s[i] in guide.values():
                    result.append(s[i])
                else:
                    if guide[s[i]] == result[-1]:
                        result.pop()
                    else:
                        return False
        if len(result) > 0:
            return False
        return True

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
